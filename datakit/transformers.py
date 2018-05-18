import pandas as pd
import numpy as np
from datakit.feature_tools import *

class build(object):
    def __init__(self, recipe = None):
        #instantiate object w/dataframe and recipe (can be blank)
        self.recipe = recipe
        return None

    def transform(self,data):
        X=pd.DataFrame() #this
        for i,cmd in enumerate(self.recipe):
            if type(cmd[1]) is tuple:
                args = (data,*cmd[1])
            else:
                args = (data,cmd[1])
            addMe = cmd[0](*args)
            X = concat(X,addMe) #this is actually the only thing unique to this one
        return X


'''
class xbuilder(build):
    def __init__():
        build.__init__(self,recipe = None)
        return None

class xcleaner(build):
    def __init__():
        build.__init__(self,recipe=None)
        return None




##specific to building X table... maybe abstract this out and this object can be general use??
##omfg... use as a constructor for specific child classes.
