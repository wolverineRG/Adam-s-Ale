# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 07:55:37 2019

@author: Logan
"""

import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Water impurity analysis tool for Ahmednagar")
data=pd.read_csv(r'Ahemadnagar.csv')

yr=input("Enter the year for which you want to know your region's water pollution content")
yr=int(yr)
x=data.iloc[:,6:7]
y1iron=data.iloc[:,0:1]
yflouride=data.iloc[:,1:2]
ysalinity=data.iloc[:,2:3]
ynitrate=data.iloc[:,3:4]
yarsenic=data.iloc[:,4:5]
yother=data.iloc[:,5:6]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y1iron,test_size=1/4,random_state=0)
from sklearn.svm import SVR
regressor=SVR(kernel='linear',C=770,gamma=.2,epsilon=1)
regressor.fit(x_train,y_train.values.ravel()) 

pred0=regressor.predict([[yr]])
pred0=float(pred0)

print(pred0)







from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,yflouride,test_size=1/4,random_state=0)
from sklearn.svm import SVR
regressor=SVR(kernel='linear',C=770,gamma=.2,epsilon=1)
regressor.fit(x_train,y_train.values.ravel()) 

pred1=regressor.predict([[yr]])
pred1=float(pred1)

print(pred1)










from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,ynitrate,test_size=1/4,random_state=0)
from sklearn.svm import SVR
regressor=SVR(kernel='linear',C=770,gamma=.2,epsilon=1)
regressor.fit(x_train,y_train.values.ravel())

pred2=regressor.predict([[yr]])
pred2=float(pred2)

print(pred2) 













from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,ysalinity,test_size=1/4,random_state=0)
from sklearn.svm import SVR
regressor=SVR(kernel='linear',C=770,gamma=.2,epsilon=1)
regressor.fit(x_train,y_train.values.ravel()) 

pred3=regressor.predict([[yr]])
pred3=float(pred3)

print(pred3) 












from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,yarsenic,test_size=1/4,random_state=0)
from sklearn.svm import SVR
regressor=SVR(kernel='linear',C=770,gamma=.2,epsilon=1)
regressor.fit(x_train,y_train.values.ravel())
pred4=regressor.predict([[yr]])
pred4=float(pred4)

print(pred4) 












from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,yother,test_size=1/4,random_state=0)
from sklearn.svm import SVR
regressor=SVR(kernel='linear',C=770,gamma=.2,epsilon=1)
regressor.fit(x_train,y_train.values.ravel())

pred5=regressor.predict([[yr]])
pred5=float(pred5)

print(pred5)

objects = ('Iron', 'Flouride', 'Nitrate','Salinity','Arsenic', 'Other')
y_pos = np.arange(len(objects))
performance = [pred0,pred1,pred2,pred3,pred4,pred5]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Impurities in PPM')
plt.title('Predicted Graph for prominent water impurities at your home')
plt.savefig('public/images/pollutionpred.png')

