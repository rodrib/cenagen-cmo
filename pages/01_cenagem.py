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

######### dataframe

import pandas as pd

# Especifica la ruta del archivo CSV
file_path = 'etl_cenagen1.csv'

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv(file_path)

# Eliminar las filas con valores nulos
df = df.dropna()


# Verificar el tipo de dato de la columna 'EDAD'
print("el tipo es", df['EDAD'].dtype)

unique_values = df['EDAD'].unique()
print(unique_values)

# Eliminar espacios en blanco al principio y al final
df['EDAD'] = df['EDAD'].str.strip()

# Convertir a numérico, forzando los valores no convertibles a NaN
df['EDAD'] = pd.to_numeric(df['EDAD'], errors='coerce')

# Eliminar filas con NaN (donde la conversión falló)
df = df.dropna(subset=['EDAD'])

# Convertir la columna a enteros (si es necesario)
df['EDAD'] = df['EDAD'].astype(int)

print(df['EDAD'].dtype)
###########
# Creamos el objeto Data de Vizzu
data = Data()
# Adicionamos los datos ordenados por edad
data.add_df(df.sort_values('EDAD'))

# Creamos el objeto story con la Data cargada
story = Story(data)

# Definimos el ancho y alto del visor de Vizzu
story.set_size(1200, 600)
# Hanbilitamos el tooltip
story.set_feature("tooltip", True)


#### van los slides

# Comenzamos a adicionar los slides de nuestra presentación
story.add_slide(
    Slide(
        Step(
            Data.filter("(record['EDAD'] > 0)"), # Quitamos las edades en cero que corresponden a competencias en equipos
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": "EDAD",
                    "y": {"set": "count()", "range": {"min": "auto", "max": "110%"},"title":"Medals"},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": "count()",
                    "title": "Test Cenagem",
                    "subtitle":"Dataset de pacientes con CMO",
                }
            ),
            Style(
                {
                    "fontFamily": 'Poppins',
                    "title": {"fontSize": 30,"color":'#735497FF',"fontWeight":"bold"},
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#735497",
                        },
                    }
                }
            ),
            
        )
    )
)

cols = st.columns([2,10,2])

with cols[0]:
    story.play()