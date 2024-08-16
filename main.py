# Import libraries
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt



# Page title
st.set_page_config(page_title='Analisis de datos del CENAGEN', page_icon='📊')
st.title('📊 Analisis de datos del CENAGEN')

# App description - Explain functionalities in an expander box
with st.expander('Sobre esta app'):
  st.markdown('**¿Qué puede hacer esta aplicación??**')
  st.info('Esta aplicación muestra el uso de Pandas para la gestión de datos, Altair para la creación de gráficos y un marco de datos editable para la interacción de datos.')
  st.markdown('**How to use the app?**')
  st.warning('Para interactuar con la aplicación, 1. Seleccione el gen de su interés en el cuadro de selección')


##############
import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np
from local_components import card_container
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch


import pandas as pd

# Especifica la ruta del archivo CSV
file_path = 'df_completo1.csv'

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv(file_path)

# Eliminar las filas con valores nulos
df = df.dropna()

# Crear un selector de año
ano_seleccionado = st.selectbox("Seleccione el gen", options=df['nombre-genes'].unique())

# Filtrar el DataFrame según el año seleccionado
df_filtrado = df[df['nombre-genes'] == ano_seleccionado]

# Mostrar el DataFrame filtrado en la interfaz de usuario
st.subheader(f"Datos del gen seleccionado {ano_seleccionado}")

# Opción para mostrar todos los valores
mostrar_todos = st.checkbox("Mostrar todos los valores")

# Mostrar los primeros 5 valores o todos según la selección del usuario
if mostrar_todos:
    ui.table(data=df_filtrado, maxHeight=300)
else:
    ui.table(data=df_filtrado.head(), maxHeight=300)

# Renderizar la tabla
st.write(ui.table)