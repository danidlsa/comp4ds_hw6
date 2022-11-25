
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
import numpy as np

#a. Load the data.

def diabetes_data():
    url="https://raw.githubusercontent.com/MargheritaPhilipp/comp4ds_hw5/main/Notebook/sample_diabetes_mellitus_data.csv"
    df = pd.read_csv(url)
    return df


#b. Split the data between train and test. (you can use train_test_split from sklearn or any other
#way)

# Leaving a function to split train/test after doing transformations


def training(X, y):
    seed=1
    X_train, X_test, y_train, y_test= train_test_split(X, y, random_state = seed, train_size = .80)
    return X_train, X_test, y_train, y_test


#c. Remove those rows that contain NaN values in the columns: age, gender, ethnicity.


def drop_selected_nans(var_list, df):
    df.dropna(subset=var_list, inplace=True)
    return df

#d. Fill NaN with the mean value of the column in the columns: height, weight.

def fill_nans(var_list, df):
    for v in var_list:
        df[v]= np.where(pd.isna(df[v])==True, 
                                   df[v].mean(),
                                   df[v])
    return df


#e. Generate dummies for ethnicity column (One hot encoding).

def one_hot_enc(df, var):
    var_data= pd.get_dummies(df[var], drop_first=True)
    df = df.join(var_data)
    return df


#f. Create a binary variable for gender M/F.

def create_binary(df, binary_var_original, binary_var_newname):
    df[binary_var_newname] = pd.get_dummies(df[binary_var_original], drop_first=True)
    return df

    
#g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the
#train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’,
#‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target the
#column: ‘diabetes_mellitus’
 

def select_features_target(df, features_list, target):
    X=df.loc[:,features_list]
    y=df.loc[:,[target]]
    return X, y

#Scale features

def scale_function(x_train, x_test):
    scaler=StandardScaler()
    x_train_scaled= scaler.fit_transform(x_train)
    x_test_scaled=scaler.transform(x_test)
    return x_train_scaled, x_test_scaled


# Create regressor

def regressor(x_train, y_train, target_name):
    clf= LogisticRegression(random_state=0).fit(x_train, np.array(y_train[target_name]))
    return clf



#h. Predict the targets for both the train and test sets and add the prediction as a new column (use
#predict_proba from the model to get the predicted probabilities) name the new column something like predictions.

def predict_from_regression(regressor, x_train_scaled, x_test_scaled, x_train, x_test):
    predict_train = regressor.predict_proba(x_train_scaled)
    predict_test = regressor.predict_proba(x_test_scaled)
    df_train = pd.DataFrame(predict_train, columns = ['0','1'])
    df_test = pd.DataFrame(predict_train, columns = ['0','1'])
    x_train["predictions"]=df_train["1"]
    x_test["predictions"]=df_test["1"]
    return predict_train, predict_test
    return x_train, x_test




#i. Compute the train and test roc_auc metric using roc_auc_score from sklearn..

def roc(y_train, x_train_scaled, regressor):
    roc_score=roc_auc_score(y_train, regressor.predict_proba(x_train_scaled)[:, 1])
    return roc_score

