import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from PIL import Image

df = pd.read_csv('./diamonds.csv')

df2 = df.iloc[:,[0,1,2,3,4,5,7,8,9,6]]

col_name = df2.select_dtypes(include=['int','float']).columns

for i in col_name:
  mean = df2[i].mean()
  med =  df2[i].median()

def outliers(col_name):
  Q1 = np.percentile(df2[col_name], 25,
                   interpolation = 'midpoint')
 
  Q3 = np.percentile(df2[col_name], 75,
                   interpolation = 'midpoint')
  IQR = Q3 - Q1

  upper = Q3+(1.5*IQR)
  lower = Q1-(1.5*IQR)
  df2.drop(df2[(df2[col_name] > upper) | (df2[col_name] < lower)].index, inplace=True)

X = df2.iloc[:,:9]
y = df2['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

X_train_cat = X_train.select_dtypes(include=['object'])

color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}

X_train_cat['color'] = X_train_cat['color'].apply(lambda x : color_encoder[x])

le=LabelEncoder()
X_train_cat['cut']=le.fit_transform(X_train_cat['cut'])
X_train_cat['clarity']=le.fit_transform(X_train_cat['clarity'])

X_train_num = X_train.select_dtypes(include=['int64', 'float64'])

X_train_cn = pd.concat([X_train_cat,X_train_num], axis=1)

scaler = StandardScaler()

X_train_new = pd.DataFrame(scaler.fit_transform(X_train_cn),columns = X_train_cn.columns,index = X_train_cn.index)

X_test_cat = X_test.select_dtypes(include=['object'])

color_encoder = {'J':1, 'I':2, 'H':3, 'G':4, 'F':5, 'E':6, 'D':7}

X_test_cat['color'] = X_test_cat['color'].apply(lambda x : color_encoder[x])
X_test_cat['cut']=le.fit_transform(X_test_cat['cut'])
X_test_cat['clarity']=le.fit_transform(X_test_cat['clarity'])

X_test_num = X_test.select_dtypes(include=['int64', 'float64'])

X_test_cn = pd.concat([X_test_cat,X_test_num], axis=1)

X_test_new = pd.DataFrame(scaler.transform(X_test_cn),columns = X_test_cn.columns,index = X_test_cn.index)

class KNN_Regression:
    def __init__(self,k):
        self.k=k
        
    def fit_func(self,X,y):
        self.X=np.asarray(X)
        self.y=np.asarray(y)
        
    def predict_func(self,X):
        X=np.asarray(X)
        predict=[]
        for x in X:
            distance=np.sqrt(np.sum((x-self.X)**2,axis=1))
            sort_value=distance.argsort()
            sort_value=sort_value[:self.k]
            predict.append(np.mean(self.y[sort_value]))
        return np.array(predict)
Model=KNN_Regression(k=3)
Model.fit_func(X_train_new,y_train)
y_pred_KNN=Model.predict_func(X_test_new)

scratch_acu=metrics.r2_score(y_test,y_pred_KNN)

regressor = KNeighborsRegressor()
regressor.fit(X_train_new, y_train)
y_test_pred = regressor.predict(X_test_new)
sk_acu=metrics.r2_score(y_test,y_test_pred)

import streamlit as st
import pickle

#model = pickle.load(open('random.pkl','rb'))

def welcome():
    return 'welcome all'


def prediction(carat,cut,color,clarity,x,y,z,depth,table):
    prediction = Model.predict(
        [[carat,cut,color,clarity,x,y,z,depth,table]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    st.title("Know your Diamond")
    st.subheader('Anatomy of Diamond')
    img = Image.open("d.png") 
    st.image(img, width=700)
    st.subheader('Quality of the Cut')
    img = Image.open("e.jfif") 
    st.image(img, width=700)
    st.subheader('Color of the Diamond')
    img = Image.open("f.jfif") 
    st.image(img, width=700)
    st.subheader('Clarity of the Diamond')
    img = Image.open("g.jfif") 
    st.image(img, width=700)
    st.title("Predict the diamond price")
    st.subheader("Enter details of diamond below to predict it`s price")
    carat = st.text_input("Weight")
    cut = st.text_input("Quality of the cut")
    color = st.text_input("Color")
    clarity = st.text_input("Clarity")
    x = st.text_input("Length(mm)")
    y = st.text_input("Width(mm)")
    z = st.text_input("Depth(mm)")
    depth = st.text_input("Total depth(%)")
    table = st.text_input("width of top of diamond relative to widest point")
    result = ""

    if st.button("Predict"):
        result = prediction(carat,cut,color,clarity,x,y,z,depth,table)
    st.success('The price of your diamond is  {}'.format(result))
    st.title('Exploratory Data Analysis')
    st.subheader('Covariance in dataset')
    st.dataframe(df.cov())

    st.subheader('Satistical Analysis')    
    st.dataframe(df.describe())

    st.subheader('Correlation')  
    st.dataframe(df.corr())


if __name__ == '__main__':
    main()

