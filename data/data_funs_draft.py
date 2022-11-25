#####

#at the end copy into three folders - possibly the following:
# load data
# process data
# run model

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
import numpy as np

# a) Create a class with a primary method that loads the data
# and returns two dataframes, one for train and another for test.
# Internally, the class can use the function defined in hw5.

#not workin - try iloc instead

class create_data():
    def __init__(self, data_loc):
        self.df = pd.read_csv(data_loc)
        self.tar = self.df.iloc[:,-1]
        self.var = self.df.iloc[:,:-1]
    
    def split(self):
        X_train, X_test, y_train, y_test = train_test_split(self.var, self.tar, random_state = 2, train_size = .80)
        #return  X_train, X_test, y_train, y_test

        df_train = pd.concat([X_train, y_train], axis= 1)
        df_test = pd.concat([X_test, y_test], axis=1)
        return df_train, df_test
    
diabetes_data = create_data("https://raw.githubusercontent.com/MargheritaPhilipp/comp4ds_hw5/main/hw5_files/sample_diabetes_mellitus_data.csv")

diabetes_train, diabetes_test = diabetes_data.split()

diabetes_train
diabetes_test

        
# testing ground - can be deleted at the end
diabetes_data.df[diabetes_data.var]

diabetes_data.tar
diabetes_data.var

def diabetes_data():
    url="https://raw.githubusercontent.com/MargheritaPhilipp/comp4ds_hw5/main/hw5_files/sample_diabetes_mellitus_data.csv"
    df = pd.read_csv(url)
    return df

df = diabetes_data()
df.iloc[:,-1]

df.columns[-1]
df.columns[:-1]


# b) Create a preprocessor class that removes those rows that contain NaN values in the columns:
# age, gender, ethnicity.
        
<<<<<<< Updated upstream
class clean_demographics():
=======
df_test_clean1 = clean_demographics(diabetes_test)        
df_test_clean1.df
df_test_clean1= df_test_clean1.drop_selected_nans()        
    
>>>>>>> Stashed changes


# c) Create a preprocessor class that fills NaN with the mean value of the column in the columns:
# height, weight.

class clean_measurements():

    


df_test_clean2 = clean_measurements(df_test_clean1).fill_nans()


# d) Create at least two feature classes that transform some of the columns in the data set.
# These feature classes need to have the same structure defined by an abstract parent class
# (Remember: polymorphism).


    # suggested features: one-hot encoding for dummies on a couple of categorical ones
    # e.g. hospital_admit_source  OR 	icu_admit_source

df_test_eth= ethnicity_oh(df_test_clean2).one_hot_enc()

df_test_gender= gender_oh(df_train_eth).one_hot_enc()


# e) Create a model class with two primary methods: train and predict.
# When the model class is initialized, the constructor (init) should receive as inputs (at least):
# 1. Feature columns that are going to be used
# 2. Target column that is going to be used
# 3. (bonus) Hyperparameters of the model to be used.

class Train_and_predict_RF:
    def __init__(self, features_list:list, 
                 target:str, 
                 df_train,
                 df_test,
                 n_estimators:int, # hyperparameter tunning 1
                 max_depth:int): # hyperparameter tunning 2
        self.X_train=df_train.loc[:,features_list]
        self.y_train=df_train.loc[:,[target]]
        self.target=target
        self.X_test=df_test.loc[:,features_list]
        self.y_test=df_test.loc[:,[target]]
        self.n_estimators=n_estimators
        self.max_depth=max_depth
        
    def train(self):
        self.model_tree= RandomForestClassifier(random_state=0,
                                                max_depth=self.max_depth,
                                                n_estimators=self.n_estimators)
        self.model_tree.fit(self.X_train, self.y_train)
        return self.model_tree
    
    def predict(self):
        self.y_pred = self.model_tree.predict(self.X_test)
        self.acc = accuracy_score(self.y_test, self.y_pred)
        return print("Accuracy of the Random Forest model: " + str(self.acc))
        

# test

features = ['age','height','weight','aids','cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']

model_randomf = Train_and_predict_RF(features, "diabetes_mellitus", df_train_gender, df_test_gender, 8, 4)

model_randomf.train()

model_randomf.predict()

# f) The model class should have as private attributes each of the inputs of the constructor 
# and an additional one, called “model” that will be a model from sklearn chosen by the team
# (such as LogisticRegression or RandomForestClassifier) as a public attribute of the class.

# 1. The train method should receive the train data containing at least the feature and target columns defined
# and fit the self.model on the train data using the features and the target (to filter columns)
# passed when the class is initialize, and return nothing.

# 2.The predict method should receive a dataframe, use the features passed to filter the columns and return
# the predicted probabilities using the .predict_proba method of the sklearn class selected.
