
import pandas as pd

from sklearn.model_selection import train_test_split


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
    