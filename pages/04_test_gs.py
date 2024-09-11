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


# Mostrar las columnas del DataFrame en Streamlit
st.write("Columnas disponibles en el DataFrame:")
st.write(df.columns)

# Seleccionar columnas usando Streamlit
columnas_seleccionadas = st.multiselect(
    'Selecciona las columnas que deseas ver:',
    df.columns
)

# Mostrar el nuevo DataFrame con las columnas seleccionadas
if columnas_seleccionadas:
    nuevo_df = df[columnas_seleccionadas]
    st.write("Nuevo DataFrame con las columnas seleccionadas:")
    st.dataframe(nuevo_df)
else:
    st.write("Por favor, selecciona al menos una columna.")

####
# Subtítulo "Genes vs Impacto"
st.subheader("Genes vs Impacto")

# Filtro por la columna "Tiene resultado"
tiene_resultado = st.selectbox('Filtrar por "Tiene resultado":', options=['SI', 'NO'])

# Filtrar el DataFrame si el usuario selecciona "SI"
if tiene_resultado == 'SI':
    df_filtrado = df[df['Tiene resultado'] == 'SI'][['Gen', 'tipo', 'EXON', 'var-gen', 'var-prot', 'Impacto', 'Tiene otra?']]
else:
    df_filtrado = df[df['Tiene resultado'] == 'NO'][['Gen', 'tipo', 'EXON', 'var-gen', 'var-prot', 'Impacto', 'Tiene otra?']]

# Mostrar el nuevo DataFrame
st.write("Nuevo DataFrame filtrado:")
st.dataframe(df_filtrado)