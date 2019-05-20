# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:01:21 2019

@author: SantiSwaroop
"""

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

#Importing the dataset
dataset=pd.read_csv('Book1.csv')

X=dataset.iloc[:,1:2].values  
Y=dataset.iloc[:,1].values

#splitting dataset into training set and testing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/4,random_state=0)    

# Fittting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)      

#Predicting the test results
Y_pred=regressor.predict(X_test)
print(Y_pred)

# plt.plot(X_test,Y_pred)
# plt.scatter(X_test,Y_test,color="Red"z
