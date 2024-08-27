import streamlit as st
import pandas as pd
from ipyvizzu import Config, Data, Style # https://ipyvizzu.vizzuhq.com/latest/
from ipyvizzustory import Story, Slide, Step # https://vizzu-story.vizzuhq.com/latest/
import math
 
# Definimos los parámetros de configuración de la aplicación
st.set_page_config(
    page_title="Cenagem", #Título de la página
    page_icon="🏃‍➡️", # Ícono
    layout="wide", # Forma de layout ancho o compacto
    initial_sidebar_state="expanded" # Definimos si el sidebar aparece expandido o colapsado
)

estilos = """
        <style>
        h2,
            div[data-testid="stMetricValue"]{
            color: #735497
            }
        body {
            background-color: #f8f8f9
        }
        </style>
"""
st.html(estilos)