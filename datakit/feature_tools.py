import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

#adding new things
def concat(df,addMe):
    return pd.concat([df,customdf],axis=1)

def columns(df,col_names):
    return df[col_names]

def dummies(df,col_name):
    return pd.get_dummies(df[[col_name]],drop_first=True)

def poly(df,col_names):
    data = df[col_names]
    p = PolynomialFeatures(2).fit(data)
    features = pd.DataFrame(p.transform(data), columns=p.get_feature_names(data.columns))
    return features

def scaled(df):
    scaled = StandardScaler().fit_transform(df.values)
    return pd.DataFrame(scaled, index=df.index, columns=df.columns)

def manual(df,customdf):
    return customdf

def mapfunc(df,col_name,lambdafunc):
    return pd.DataFrame(df[col_name].map(lambdafunc))

#modifying existing tables
def drop(df,col_names):
    return df.drop(col_names,axis=1)
