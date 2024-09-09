import streamlit as st
import pandas as pd
import plotly.express as px 

# Definimos los parámetros de configuración de la aplicación
st.set_page_config(
    page_title="Demo carga datos desde Google Sheets", #Título de la página
    page_icon="📊", # Ícono
    layout="wide", # Forma de layout ancho o compacto
    initial_sidebar_state="expanded" # Definimos si el sidebar aparece expandido o colapsado
)

gsheetid='1jAdbksm3fu5uVE7NOGe7LtSSJBjQGEPzc0c44f9Ud4s'
sheetid='0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}&format'
st.write(url)


df = pd.read_csv(url)
#https://docs.google.com/spreadsheets/d/1jAdbksm3fu5uVE7NOGe7LtSSJBjQGEPzc0c44f9Ud4s/edit?usp=sharing

# Mostrar el DataFrame usando st.dataframe()
st.dataframe(df)  # Esta función permite desplazarse por la tabla si es necesario