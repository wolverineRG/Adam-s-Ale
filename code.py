


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
print("Welcome to the rainfall prediction tool for Maharashtra region")



super_s=input("press 2 for Konkan and goa \n 1 for madhya maharashtra \n 3 for marathawada  \n 4 for vidarbha ")
wateer=input("Please enter the amount of water located for your region")
if super_s==1:
    
    data=pd.read_csv(r'raintt.csv')
    annual_val=158.056 + 881.436
    jf=4.451+7.269 #taking average along + the standard deviation for avg rain fall in jan and feb
    mam=35.384+24.325 #taking average along + the standard deviation for avg rain fall in march,april and may
    jjas=739.744+142.1863 #taking average along + the standard deviation for avg rain fall in june,july ,sept and august
    ond=101.8436+57.05686 #taking average along + the standard deviation for avg rain fall in oct,nov and dec
    jfinal=jf
    mamfinal=mam
    jjasfinal=jjas
    ondfinal=ond
    
    
elif super_s==2:
    data=pd.read_csv(r'kandg.csv')
    annual_valkag=2987.531624 + 486.9207131
    jfkg=1.782905983+4.351660218
    mamkg= 38.93162393+58.18392012
    jjaskg= 2804.186325+459.3226643
    ondkg= 142.6299145+95.20484473
    jfinal=jfkg
    mamfinal=mamkg
    jjasfinal=jjaskg
    ondfinal=ondkg
    
elif super_s==3:
    data=pd.read_csv(r'marathwada.csv')
    annual_valm=791.7452991+188.1718425
    jfm=9.313675214+13.19983611 #taking average along + the standard deviation for avg rain fall in jan and feb
    mamm=30.07435897+26.75683011 #taking average along + the standard deviation for avg rain fall in march,april and may
    jjasm=663.7794872+168.6823405 #taking average along + the standard deviation for avg rain fall in june,july ,sept and august
    ondm=88.57264957+58.89364848
    jfinal=jfm
    mamfinal=mamm
    jjasfinal=jjasm
    ondfinal=ondm
    
else:
    data=pd.read_csv(r'vidarbha.csv')
    annual_valv=1093.54359+203.6672469
    jfv=22.21111111+22.86632737#taking average along + the standard deviation for avg rain fall in jan and feb
    mamv=32.72478632+26.6398001 #taking average along + the standard deviation for avg rain fall in march,april and may
    jjasv=963.1051282+182.9170449 #taking average along + the standard deviation for avg rain fall in june,july ,sept and august
    ondv=75.4974359+50.65250864
    jfinal=jfv
    mamfinal=mamv
    jjasfinal=jjasv
    ondfinal=ondv
    
    
a=input("Enter the year for which you want the rain fall to be predicted")
b=input("Enter the month for which you would like the rainfall to be predicted\n press 1 for January \n press 2 for february \n press 3 for March \n press 4 for April\n press 5 for May\n press 6 for June \n press 7 for July\n press 8 for August\n press 9 for September \n press 10 for October\n press 11 for November\n press 12 for December \n Enter Your Choice \n ")
data=pd.read_csv(r'raintt.csv')


i=1

i=int(i)
b=int(b)
# print("Rainfall for the current month")
while True:
    if b==1:
        x1=data.iloc[:,[1,14,15]]
        y=data.iloc[:,2:3]
        c=jfinal
    
    
    elif b==2:
        x1=data.iloc[:,[1,14,15]]
        y=data.iloc[:,3:4]
        c=jfinal
    
    elif b==3:
            x1=data.iloc[:,[1,14,16]]
            y=data.iloc[:,4:5]
            c=mamfinal    
    
    elif b==4:
        x1=data.iloc[:,[1,14,16]]
        y=data.iloc[:,5:6]
        c=mamfinal
    
    elif b==5:
        x1=data.iloc[:,[1,14,16]]
        y=data.iloc[:,6:7]
        c=mamfinal
    elif b==6:
        x1=data.iloc[:,[1,14,17]]
        y=data.iloc[:,7:8]
        c=jjasfinal
    elif b==7:
        x1=data.iloc[:,[1,14,17]]
        y=data.iloc[:,8:9]
        c=jjasfinal
    elif b==8:
        x1=data.iloc[:,[1,14,17]]
        y=data.iloc[:,9:10]
        c=jjasfinal
    elif b==9:
        x1=data.iloc[:,[1,14,17]]
        y=data.iloc[:,10:11]
        c=jjasfinal
    elif b==10:
        x1=data.iloc[:,[1,14,18]]
        y=data.iloc[:,11:12]
        c=ondfinal
    elif b==11:
        x1=data.iloc[:,[1,14,18]]
        y=data.iloc[:,12:13]
        c=ondfinal
    elif b==12:
        x1=data.iloc[:,[1,14,18]]
        y=data.iloc[:,13:14]
        c=ondfinal   

        
        
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x1,y,test_size=1/4,random_state=0)
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit_transform(x_train,y_train)
 
    from sklearn.tree import DecisionTreeRegressor
    cid = DecisionTreeRegressor(max_depth=10)
    cid.fit(x_train,y_train)
    y_predict=cid.predict(x_test)
    ar=np.array([[a,b,c]])
    pred=cid.predict(ar)
    pred=float(pred)
    # print("Rainfall for ",i,"month------------------------>:")
    pre=str(pred)
    print(pre+"mm")
    
    i=i+1
    b=b+1
    
    if(i>3 or b>12):
        break
    
    
    
    
    

    

    






dataset=pd.read_csv('Book1.csv')

X=dataset.iloc[:,2:3].values  
Y=dataset.iloc[:,1:2].values



#splitting dataset into training set and testing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0)    

# Fittting simple linear regression to the training set
from sklearn.svm import SVR
regressor=SVR(kernel='linear',C=770,gamma=.2,epsilon=1)
regressor.fit(X_train,Y_train.ravel()) 
Y_pres=regressor.predict(X_test)
#plt.plot(X_test,Y_pres)
#plt.scatter(X_test,Y_test,color='red')     

#Predicting the test results
j=0
while True:
   Y_pred=regressor.predict([[b+j]])
   if super_s==1:
       Y_pred=Y_pred*(21.9/100)
   elif super_s==2:
       Y_pred=Y_pred*(28.7/100)
   elif super_s==3:
       Y_pred=Y_pred*(16.13/100)
   elif super_s==4:
       Y_pred=Y_pred*(20.86/100)
       
   Y_pred=float(Y_pred)
#    print('\n demand for month ',j+1,'month--------------->  \n')
    #code for the ideal water demand
   ideal_demand=(Y_pred*0.083*1.3)+(Y_pred*0.087*1.7)+(Y_pred*0.0955*2.2)+(Y_pred*0.083*2.7)+(Y_pred*0.637*3.4)

   ideal= str(ideal_demand)   
   print(ideal+"Liters")
   
   
   j=j+1
   if(j>=3 or b>12):
        break