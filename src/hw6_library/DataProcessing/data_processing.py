import pandas as pd

import numpy as np

from abc import ABC, abstractmethod

# b) Create a preprocessor class that removes those rows that contain NaN values in the columns:
# age, gender, ethnicity.
        
class clean_demographics():
    def __init__(self, df):
        self.vars_to_clean=["age", "gender", "ethnicity"]
        self.df=df.copy()
        
    def drop_selected_nans(self):
        self.df.dropna(subset=self.vars_to_clean, inplace=True)
        return self.df
    
    


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
