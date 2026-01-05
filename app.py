# -*- coding: utf-8 -*-
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Analisis de Datos de Vehiculos")

# Load CSV
try:
    car_data = pd.read_csv("vehicles_us.csv")
    st.write("CSV cargado correctamente")
    st.write(car_data.head())
except Exception as e:
    st.error(f"Error cargando CSV: {e}")

# Histogram
if 'car_data' in locals():
    st.subheader("Histograma del odómetro")
    fig1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Diagrama de dispersión de odómetro vs precio")
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)




