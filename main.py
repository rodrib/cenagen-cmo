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
file_path = 'etl_cenagen1.csv'

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
#st.write(ui.table)


#### Graficos




# Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts = df['CM'].value_counts().reset_index()
resumen_counts.columns = ['CM', 'Cantidad']

# Mostrar el conteo de valores para verificar
st.write("Conteo de valores en 'CM':")
#st.write(resumen_counts)

ui.table(data=resumen_counts, maxHeight=300)

#st.write(ui.table)


data = {
    "CM": [
        "0", "1", "sd", "2", "CO", "3", "CO bilat", 
        "Melanoma", "unilat", "ca colorrectal", 
        "CO unil izq", "0 (quiste benigno en ovario)", 
        "CO unil", "2//1"
    ],
    "Cantidad": [34, 22, 22, 15, 9, 4, 2, 2, 1, 1, 1, 1, 1, 1]
}


# Crear el DataFrame
df1 = pd.DataFrame(data)

# Ordenar los datos por 'Cantidad' de mayor a menor
df1 = df1.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order = df1['CM'].tolist()

# Mostrar el gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de CM")
with card_container(key="chart2"):
    st.vega_lite_chart(df1, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(173, 250, 29)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'CM', 'type': 'ordinal', 'axis': {'title': 'CM'}, 'sort': category_order},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)

### ETNIA

# Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts_etnia = df['ETNIA'].value_counts().reset_index()
resumen_counts_etnia.columns = ['ETNIA', 'Cantidad']

# Mostrar el conteo de valores para verificar
st.write("Conteo de valores en 'ETNIA':")
#st.write(resumen_counts)

ui.table(data=resumen_counts_etnia, maxHeight=300)



# Crear el diccionario con los datos
data_etnia = {
    "ETNIA": ["sd", "1", "0", "0/1", "italianos"],
    "Cantidad": [55, 43, 13, 4, 1]
}

# Convertir a DataFrame
df_etnia = pd.DataFrame(data_etnia)

# Ordenar los datos por 'Cantidad' de mayor a menor
df_etnia = df_etnia.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order_etnia = df_etnia['ETNIA'].tolist()

# Mostrar el gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de ETNIA")
with card_container(key="chart2"):
    st.vega_lite_chart(df_etnia, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(0, 153, 76)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'ETNIA', 'type': 'ordinal', 'axis': {'title': 'ETNIA'}, 'sort': category_order_etnia},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)


### EDAD

# Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts_edad = df['EDAD'].value_counts().reset_index()
resumen_counts_edad.columns = ['EDAD', 'Cantidad']

# Mostrar el conteo de valores para verificar
st.write("Conteo de valores en 'EDAD':")
#st.write(resumen_counts)

ui.table(data=resumen_counts_edad, maxHeight=300)


# Crear el diccionario con los datos
data_edad = {
    "EDAD": [
        "sd", 37, 40, 38, 44, 64, 42, 45, 65, 57, 41, 29, 59, 43, 26, 
        49, 53, 54, 51, 28, 61, 48, 22, 36, 50, "fallecida", 31, 19, 
        17, 66, 32, 20, 39, 73, 56, 34, 27, 52, 70, 30, 16, 71, 35, 
        18, 60
    ],
    "Cantidad": [
        26, 7, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ]
}

# Convertir a DataFrame
df_edad = pd.DataFrame(data_edad)

# Ordenar los datos por 'Cantidad' de mayor a menor
df_edad = df_edad.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order_edad = df_edad['EDAD'].tolist()

# Mostrar el gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de EDAD")
with card_container(key="chart2"):
    st.vega_lite_chart(df_edad, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(0, 153, 76)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'EDAD', 'type': 'ordinal', 'axis': {'title': 'EDAD'}, 'sort': category_order_edad},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)

#### Accesion



# Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts_accession = df['Accession'].value_counts().reset_index()
resumen_counts_accession.columns = ['Accession', 'Cantidad']

# Mostrar el conteo de valores para verificar
st.write("Conteo de valores en 'Accession':")
#st.write(resumen_counts)

ui.table(data=resumen_counts_accession, maxHeight=300)

# Datos proporcionados
data_accesion = {
    "Accession": [
        "sd", "VCV000037569.", "VCV000037698.", "VCV000038043.", 
        "VCV000219665.", "VCV000054398.", "VCV000005591.", "VCV000017674.", 
        "VCV000054200.", "VCV000017661.", "VCV000017693.", "VCV000017677.", 
        "VCV000491087.", "VCV000009322.", "VCV000055523.", "VCV000548311.", 
        "VCV000055360.", "VCV000548237.", "VCV000038015.", "VCV000037691.", 
        "VCV000037516.", "VCV000266170.", "VCV000037409.", "VCV000009342.", 
        "VCV000054584.", "VCV000418999.", "VCV000017675.", "VCV000037786.", 
        "VCV000548363.", "VCV000051070.", "VCV000038122.", "VCV000038242.", 
        "VCV000052792.", "VCV000037636.", "VCV000234828.", "VCV000037623.", 
        "VCV000055531.", "VCV000038082.", "VCV000229950.", "VCV000055157.", 
        "VCV000052709.", "VCV000037616.", "VCV000055502.", "VCV000037429.", 
        "VCV000185292.", "VCV000052122.", "VCV000038227.", "VCV000037406.", 
        "VCV000037763."
    ],
    "Cantidad": [
        11, 10, 6, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ]
}


# Verificar las longitudes de las listas
print(f"Longitud de 'Accession': {len(data_accesion['Accession'])}")
print(f"Longitud de 'Cantidad': {len(data_accesion['Cantidad'])}")

# Convertir a DataFrame
df_accesion = pd.DataFrame(data_accesion)




# Ordenar los datos por 'Cantidad' de mayor a menor
df_accesion = df_accesion.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order_accession = df_accesion['Accession'].tolist()

# Mostrar el gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de Variantes")
with card_container(key="chart2"):
    st.vega_lite_chart(df_accesion, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(0, 153, 76)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'Accession', 'type': 'ordinal', 'axis': {'title': 'Accession'}, 'sort': category_order_accession},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)


### RECIDIVA

# Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts_recidiva = df['RECIDIVA'].value_counts().reset_index()
resumen_counts_recidiva.columns = ['RECIDIVA', 'Cantidad']

# Mostrar el conteo de valores para verificar
st.write("Conteo de valores en 'RECIDIVA':")
#st.write(resumen_counts)

ui.table(data=resumen_counts_recidiva, maxHeight=300)

# Datos proporcionados
data_recidiva = {
    "RECIDIVA": [
        "sd", "0", "1", "CM der 2001, CO 2007, CM izq 2015"
    ],
    "Cantidad": [
        109, 4, 2, 1
    ]
}

# Crear el DataFrame
df_recidiva = pd.DataFrame(data_recidiva)


# Ordenar los datos por 'Cantidad' de mayor a menor
df_recidiva = df_recidiva.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order_recidiva = df_recidiva['RECIDIVA'].tolist()

# Mostrar el gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de RECIDIVA")
with card_container(key="chart2"):
    st.vega_lite_chart(df_recidiva, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(0, 100, 76)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'RECIDIVA', 'type': 'ordinal', 'axis': {'title': 'RECIDIVA'}, 'sort': category_order_recidiva},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)

### RE1

# Contar los valores únicos en la columna 'Proyecto/tesis/Resumen'
resumen_counts_re1 = df['RE1'].value_counts().reset_index()
resumen_counts_re1.columns = ['RE1', 'Cantidad']


# Mostrar el conteo de valores para verificar
st.write("Conteo de valores en 'RE1':")
#st.write(resumen_counts)

ui.table(data=resumen_counts_re1, maxHeight=300)
