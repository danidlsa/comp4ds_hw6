import pandas as pd

import numpy as np


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
    

