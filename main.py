import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv('happy.csv')

st.title('In Search For Happiness')
country = st.text_input('Enter the name of your country:')
xaxis = st.selectbox('Select the data for the X-axis', ('GDP', 'Happiness', 'Generosity'))
yaxis = st.selectbox('Select the data for the Y-axis', ('GDP', 'Happiness', 'Generosity'))
title = st.subheader(f'{xaxis} and {yaxis}')

happy = data['happiness']
gdps = data['gdp']
general = data['generosity']
countrys = data['country']


if xaxis == 'GDP' and yaxis == 'Happiness' and country in countrys.values:
    filtered_data = data[data['country'] == country]
    figure = px.scatter(x=happy, y=gdps, labels={'x': 'happy', 'y': 'gdps'})
    st.plotly_chart(figure)
elif xaxis == 'GDP' and yaxis == 'Generosity':
    figure = px.scatter(x=general, y=gdps, labels={'x': 'general', 'y': 'gdps'})
    st.plotly_chart(figure)
#elif


