import streamlit as st
import pandas as pd
import numpy as np

import home
st.set_page_config(page_title="Pub_locations", page_icon="https://cdn.pixabay.com/photo/2014/04/02/10/45/location-304467__340.png")
st.title("Pub Location")
st.header('Select a local_authority')

option=st.selectbox('select a local_authority',home.data_selection)

'You selected: ',option

button_click=st.button('Find now')
if button_click==True:
    df_loc=home.df[home.df['local_authority']==option]
    count=df_loc.shape[0]
    st.write('Number of Pubs in this area is:', count)
    #st.subheader('Number of Pubs in this area is:',count)
    df_loc=df_loc[['latitude','longitude']]
    st.map(df_loc)