import pandas as pd


from abc import ABC, abstractmethod

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
