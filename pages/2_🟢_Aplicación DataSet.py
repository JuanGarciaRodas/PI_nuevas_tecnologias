import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")
Lugares_deportivos = pd.read_csv('./static/datasets/Lugares_deportivos.csv')
df = pd.read_csv('./static/datasets/Lugares_deportivos.csv')


tad_descripcion, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"])

#----------------- -----------------------------------------
#Generador de datos
#----------------------------------------------------------
with tad_descripcion:      

    st.markdown('''
    ## Plantilla Básica para Proyecto Integrador

    ### Introducción

    -   ¿Qué es el proyecto?
    -   ¿Cuál es el objetivo principal?
    -   ¿Por qué es importante? 

    ### Desarrollo

    -   Explicación detallada del proyecto
    -   Procedimiento utilizado
    -   Resultados obtenidos

    ### Conclusión

    -   Resumen de los resultados
    -   Logros alcanzados
    -   Dificultades encontradas
    -   Aportes personales
    ''')    

#----------------------------------------------------------
#Analítica 1
#----------------------------------------------------------
with tab_Análisis_Exploratorio:    
    st.title("Análisis Exploratorio")
    st.markdown("""
    * Muestra las primeras 5 filas del DataFrame.  **(df.head())**
    * Muestra la cantidad de filas y columnas del DataFrame.  **(df.shape)**
    * Muestra los tipos de datos de cada columna.  **(df.dtypes)**
    * Identifica y muestra las columnas con valores nulos. **(df.isnull().sum())**
    * Muestra un resumen estadístico de las columnas numéricas.  **(df.describe())**
    * Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada. **(df['columna_categorica'].value_counts())** 
    * Otra información importante           
    """)   
    
def analisis_exploratorio(df):   
 df = pd.read_csv('./static/datasets/Lugares_deportivos.csv')

 # Selector multi-select para que el usuario elija las consultas
consultas_seleccionadas = st.multiselect('Selecciona las consultas que quieres realizar:', [
    "Muestra las primeras 5 filas",
    "Muestra la cantidad de filas y columnas",
    "Muestra los tipos de datos",
    "Identifica y muestra las columnas con valores nulos",
    "Muestra un resumen estadístico",
    "Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada"
])

# Ejecutar las consultas seleccionadas
if consultas_seleccionadas:
    for consulta in consultas_seleccionadas:
        if consulta == "Muestra las primeras 5 filas":
            st.dataframe(df.head(5))
        elif consulta == "Muestra la cantidad de filas y columnas":
            st.write(f"El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.")
        elif consulta == "Muestra los tipos de datos":
            st.dataframe(df.dtypes)
        elif consulta == "Identifica y muestra las columnas con valores nulos":
            nulos_por_columna = df.isnull().sum()
            st.dataframe(nulos_por_columna[nulos_por_columna > 0])
        elif consulta == "Muestra un resumen estadístico":
            st.dataframe(df.describe())
        elif consulta == "Muestra una tabla con la frecuencia de valores únicos para una columna categórica seleccionada":
            columna = st.selectbox('Selecciona una columna categórica:', df.select_dtypes(include=['object']).columns)
            st.dataframe(df[columna].value_counts())
        else:
            st.write("Opción no válida")
else:
    st.write("Selecciona al menos una consulta")
    
 


#----------------------------------------------------------
#Analítica 2
#----------------------------------------------------------
with tab_Filtrado_Básico:
        st.title("Filtro Básico")
        st.markdown("""
        * Permite filtrar datos usando condiciones simples. **(df[df['columna'] == 'valor'])**
        * Permite seleccionar una columna y un valor para el filtro. **(st.selectbox, st.text_input)**
        * Permite elegir un operador de comparación (igual, diferente, mayor que, menor que). **(st.radio)**
        * Muestra los datos filtrados en una tabla. **(st.dataframe)** 
        """)
 

#----------------------------------------------------------
#Analítica 3
#----------------------------------------------------------
with tab_Filtro_Final_Dinámico:
        st.title("Filtro Final Dinámico")
        st.markdown("""
        * Muestra un resumen dinámico del DataFrame filtrado. 
        * Incluye información como los criterios de filtrado aplicados, la tabla de datos filtrados, gráficos y estadísticas relevantes.
        * Se actualiza automáticamente cada vez que se realiza un filtro en las pestañas anteriores. 
        """)



    




