#####

#at the end copy into three folders - possibly the following:
# load data
# process data
# run model

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

from abc import ABC, abstractmethod


import warnings
warnings.filterwarnings('ignore')

# a) Create a class with a primary method that loads the data
# and returns two dataframes, one for train and another for test.
# Internally, the class can use the function defined in hw5.

class create_data():
    def __init__(self):
        self.df = pd.read_csv("https://raw.githubusercontent.com/danidlsa/comp4ds_hw6/main/data/sample_diabetes_mellitus_data.csv")
        self.tar = self.df.iloc[:,-1]
        self.var = self.df.iloc[:,:-1]
    
    def split(self, train_size):
        X_train, X_test, y_train, y_test = train_test_split(self.var, self.tar, random_state = 2, train_size = train_size)
        df_train = pd.concat([X_train, y_train], axis= 1)
        df_test = pd.concat([X_test, y_test], axis=1)
        return df_train, df_test
    
        
# testing ground - can be deleted at the end
diabetes_data = create_data()

diabetes_train, diabetes_test = diabetes_data.split(0.8)

diabetes_train
diabetes_test
#diabetes_data.tar
#diabetes_data.var

# b) Create a preprocessor class that removes those rows that contain NaN values in the columns:
# age, gender, ethnicity.


        
class clean_demographics():
    def __init__(self, df):
        self.vars_to_clean=["age", "gender", "ethnicity"]
        self.df=df.copy()
        
    def drop_selected_nans(self):
        self.df.dropna(subset=self.vars_to_clean, inplace=True)
        return self.df
    
# test

df_train_clean1 = clean_demographics(diabetes_train)        
df_train_clean1.df
df_train_clean1= df_train_clean1.drop_selected_nans()        
        
df_test_clean1 = clean_demographics(diabetes_test)        
df_test_clean1.df
df_test_clean1= df_test_clean1.drop_selected_nans()        
    


# c) Create a preprocessor class that fills NaN with the mean value of the column in the columns:
# height, weight.



class clean_measurements():
    def __init__(self, df):
        self.vars_to_fill=["height", "weight"]
        self.df=df.copy()
        
    def fill_nans(self):
        for v in self.vars_to_fill:
            self.df[v]= np.where(pd.isna(self.df[v])==True, 
                            self.df[v].mean(),
                            self.df[v])
        return self.df
    
# test

df_train_clean2 = clean_measurements(df_train_clean1)
df_train_clean2.df
df_train_clean2.vars_to_fill
df_train_clean2 = df_train_clean2.fill_nans()


df_test_clean2 = clean_measurements(df_test_clean1).fill_nans()


# d) Create at least two feature classes that transform some of the columns in the data set.
# These feature classes need to have the same structure defined by an abstract parent class
# (Remember: polymorphism).



class Transform_features(ABC):
    def __init__(self, df):
        self.df=df
    
    @abstractmethod
    def one_hot_enc(self):
       return NotImplementedError()


class ethnicity_oh(Transform_features):
    
    def one_hot_enc(self):
        self.var_data=pd.get_dummies(self.df["ethnicity"], drop_first=False)
        self.df=self.df.join(self.var_data)
        return self.df

class gender_oh(Transform_features):

    def one_hot_enc(self):
        self.var_data=pd.get_dummies(self.df["gender"], drop_first=True) # here is the difference with the other class, this one does drop the first variable
        self.df=self.df.join(self.var_data)
        return self.df

# test

df_train_eth = ethnicity_oh(df_train_clean2)
df_train_eth = df_train_eth.one_hot_enc()

df_train_gender= gender_oh(df_train_eth).one_hot_enc()

df_test_eth= ethnicity_oh(df_test_clean2).one_hot_enc()

df_test_gender= gender_oh(df_train_eth).one_hot_enc()



# e) Create a model class with two primary methods: train and predict.
# When the model class is initialized, the constructor (init) should receive as inputs (at least):
# 1. Feature columns that are going to be used
# 2. Target column that is going to be used
# 3. (bonus) Hyperparameters of the model to be used.

# f) The model class should have as private attributes each of the inputs of the constructor 
# and an additional one, called “model” that will be a model from sklearn chosen by the team
# (such as LogisticRegression or RandomForestClassifier) as a public attribute of the class.

# 1. The train method should receive the train data containing at least the feature and target columns defined
# and fit the self.model on the train data using the features and the target (to filter columns)
# passed when the class is initialize, and return nothing.

# 2.The predict method should receive a dataframe, use the features passed to filter the columns and return
# the predicted probabilities using the .predict_proba method of the sklearn class selected.


class Train_and_predict_RF:
    def __init__(self, feature_cols, 
                 target_col, 
                 n_estimators:int, # hyperparameter tunning 1
                 max_depth:int): # hyperparameter tunning 2
        self.__features=feature_cols
        self.__target=target_col
        self.model=RandomForestClassifier(max_depth=max_depth,
                                          n_estimators=n_estimators)
        
    def train(self, df_train):  
        self.X=df_train.loc[:,self.__features]
        self.y=df_train.loc[:,[self.__target]]
        self.model.fit(self.X, self.y)
        return self.model
    
    def predict(self, df_test): 
        self.X_test= df_test.loc[:,self.__features] # filter cols
        self.y_pred = self.model.predict(self.X_test)
        return self.y_pred
    
    
# test 
features = ['age','height','weight','aids','cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis',
            'M', 'Asian', 'Hispanic', 'Native American', 'African American' ]

model_randomf = Train_and_predict_RF(features, "diabetes_mellitus", 8, 4)

model_randomf.train(df_train_gender)

model_randomf.predict(df_test_gender)

# This is working, but when adding

