import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv('happy.csv')

st.title('In Search For Happiness')
xaxis = st.selectbox('Select the data for the X-axis', ('GDP', 'Happiness', 'Generosity'))
yaxis = st.selectbox('Select the data for the Y-axis', ('GDP', 'Happiness', 'Generosity'))
title = st.subheader(f'{xaxis} and {yaxis}')

happy = data['happiness']
gdps = data['gdp']
if xaxis == 'GDP' and yaxis == 'Happiness':
    figure = px.scatter(x=happy, y=gdps, labels={'x': 'happy', 'y': 'gdps'})
    st.plotly_chart(figure)

