#####

#at the end copy into three folders - possibly the following:
# load data
# process data
# run model

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
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
        
class clean_demographics():


# c) Create a preprocessor class that fills NaN with the mean value of the column in the columns:
# height, weight.

class clean_measurements():

    

# d) Create at least two feature classes that transform some of the columns in the data set.
# These feature classes need to have the same structure defined by an abstract parent class
# (Remember: polymorphism).


    # suggested features: one-hot encoding for dummies on a couple of categorical ones
    # e.g. hospital_admit_source  OR 	icu_admit_source


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
