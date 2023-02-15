from sklearn import model_selection
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import mean_squared_error
import math
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st



df= pd.read_csv("C:\\Users\\Dell\\Downloads\\grocerydata.csv")
droplist=['Invoice ID','Quantity', 'Tax 5%', 'Total', 'Date','Time', 'Payment','cogs','gross margin percentage', 'gross income']

df_new = df.drop(droplist,axis=1)

df_one = pd.get_dummies(df_new["Branch"])
df_two = pd.get_dummies(df_new["City"])
df_three = pd.get_dummies(df_new["Customer type"])
df_five = pd.get_dummies(df_new["Product line"])


for i in range(len(df_new)):
    if df_new.iloc[i,3]=="Female":
        df_new.iloc[i,3]=1
    else:
        df_new.iloc[i,3]=0


df_new.drop(['Branch', 'City', 'Customer type', 'Product line'],inplace=True, axis=1)
df_ready=pd.concat((df_one, df_two, df_three, df_five, df_new), axis=1)


#data division for rating prediction (1)
x1=df_ready.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15]]
y1=df_ready.iloc[:,16]
min_max_scaler_object = preprocessing.MinMaxScaler()
min_max_scaler_object.fit(x1)
x1_new = min_max_scaler_object.transform(x1)

le = LabelEncoder()

    
#data division for gender prediction (2)
x2=df_ready.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16]]
y2=df_ready.iloc[:,14]
min_max_scaler_object = preprocessing.MinMaxScaler()
min_max_scaler_object.fit(x2)
x2_new = min_max_scaler_object.transform(x2)


column_name1=['A', 'B', 'C', 'Mandalay', 'Naypyitaw', 'Yangon', 'Member', 'Normal',
       'Electronic accessories', 'Fashion accessories', 'Food and beverages',
       'Health and beauty', 'Home and lifestyle', 'Sports and travel',
       'Unit price']

column_name2=['A', 'B', 'C', 'Mandalay', 'Naypyitaw', 'Yangon', 'Member', 'Normal',
       'Electronic accessories', 'Fashion accessories', 'Food and beverages',
       'Health and beauty', 'Home and lifestyle', 'Sports and travel',
       'Unit price', 'Rating']

def member(arr):
    index_want=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15)
    arr_rate=[ arr[i] for i in index_want]
    df_rate = pd.DataFrame([arr_rate] ,columns = column_name1)
    min_max_scaler_object.fit(df_rate)
    clfsvm=svm.SVR(kernel='rbf')
    clfsvm.fit(x1, y1)
    y1_pred = clfsvm.predict(df_rate)+1


    y2_svc = le.fit_transform(y2)
    index_gender=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15)
    arr_gender=[ arr[i] for i in index_gender ]
    arr_gender.append(float(y1_pred))
    df_gender = pd.DataFrame([arr_gender] ,columns = column_name2)
    min_max_scaler_object.fit(df_gender)
    clfsvc= SVC(C=10, gamma=0.1,kernel="rbf")
    clfsvc.fit(x2,y2_svc)
    y2_pred = clfsvc.predict(df_gender)
    df_y2_pred=pd.DataFrame(y2_pred,columns=['Gender'])
    df_y2_pred_final=le.inverse_transform(df_y2_pred)

    return y1_pred, df_y2_pred_final

def normal(arr):
    index_want=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15)
    arr_rate=[ arr[i] for i in index_want]
    df_rate = pd.DataFrame([arr_rate] ,columns = column_name1)
    min_max_scaler_object.fit(df_rate)
    alg1=LinearRegression()
    alg1.fit(x1, y1)
    y1_pred= alg1.predict(df_rate)
    


    y2_svc = le.fit_transform(y2)
    index_gender=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15)
    arr_gender=[ arr[i] for i in index_gender ]
    arr_gender.append(int(y1_pred[0]))
    df_gender = pd.DataFrame([arr_gender] ,columns = column_name2)
    min_max_scaler_object.fit(df_gender)
    clfknn=KNeighborsClassifier(n_neighbors=4)
    clfknn.fit(x2,y2_svc)
    y2_pred = clfknn.predict(df_gender)
    df_y2_pred=pd.DataFrame(y2_pred,columns=['Gender'])
    df_y2_pred_final=le.inverse_transform(df_y2_pred)

    return y1_pred,df_y2_pred_final

def get_data(in_arr):
    arr=[]
    for i in range(3):
        if in_arr[0]==df_ready.columns[i]:
            arr.append(1)
        else:
            arr.append(0)
    for i in range(3,6):
        if in_arr[1]==df_ready.columns[i]:
            arr.append(1)
        else:
            arr.append(0)
    
    for i in range(6,8):
        if in_arr[2]==df_ready.columns[i]:
            arr.append(1)
        else:
            arr.append(0)

    for i in range(8,14):
        if in_arr[3]==df_ready.columns[i]:
            arr.append(1)
        else:
            arr.append(0)

    arr.append(None)
    arr.append(in_arr[4])
    arr.append(None)

    if in_arr[5]=='Yes':
        rating_ans,gender_ans=member(arr)
    else:
        rating_ans,gender_ans=normal(arr)

    return rating_ans, gender_ans
