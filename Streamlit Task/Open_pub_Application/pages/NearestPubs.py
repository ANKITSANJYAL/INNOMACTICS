import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import home
st.set_page_config(page_title="NearestPubs", page_icon="🌍")
# Python code for the above approach
 
# Calculate the Euclidean distance
# between two points
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** ( 1 / 2)
 
# Function to calculate K closest points
def kClosest(points, target, K):
    pts = []
    n = len(points)
    d = []
 
    for i in range(n):
        d.append({
            "first": distance(points[i][0], points[i][1], target[0], target[1]),
            "second": i
        })
    
    
     
    d = sorted(d, key=lambda l:l["first"])
    
    for i in range(K):
        pt = []
        pt.append(points[d[i]["second"]][0])
        pt.append(points[d[i]["second"]][1])
        pts.append(pt)
   
# Calling DataFrame constructor on list
    df_nearest_loc = pd.DataFrame(pts,columns=['latitude','longitude'])
    st.subheader('Nearest five Pubs for the Latitude and longitude you entered')
    st.map(df_nearest_loc)
    
# Driver code
df_lat_log=home.df[['latitude','longitude']]
points = df_lat_log.values.tolist()

lat = st.sidebar.number_input('Enter Latitude',format="%.5f")
log = st.sidebar.number_input('Enter Longitude',format="%.6f",key=int)

target = [lat,log]
K = 5

kClosest(points, target, K)








