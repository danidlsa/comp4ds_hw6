
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


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