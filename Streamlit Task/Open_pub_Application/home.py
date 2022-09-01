
import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Home", page_icon="https://cdn-icons-png.flaticon.com/512/2/2144.png")
df=pd.read_csv('open_pubs.csv')
df.columns=['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
df = df.replace('\\N', np.NaN)
df=df.dropna()
df[['latitude', 'longitude']]=df[['latitude', 'longitude']].apply(pd.to_numeric, axis = 1)
data_selection=df.local_authority.unique()
pub="Total number of PUBS: "+str(df.shape[0])
auth="Total number of PUBS in Local Authority: "+str(data_selection.shape[0])
st.sidebar.success("select your required page")
st.title("Open PUB Application")
st.subheader('Dataset')
st.dataframe(df)
