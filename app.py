# -*- coding: utf-8 -*-
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(r"vehicles_us.csv")  # Use full path if needed

st.header('Analisis de Datos de Vehiculos')

st.write(car_data.head())

# Histogram
fig = px.histogram(car_data, x="odometer")
st.plotly_chart(fig, use_container_width=True)

# Scatter
fig2 = px.scatter(car_data, x="odometer", y="price")
st.plotly_chart(fig2, use_container_width=True)



