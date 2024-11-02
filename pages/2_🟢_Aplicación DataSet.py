import streamlit as st
import pandas as pd



st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")



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
    st.tabs(["Análisis Exploratorio"])
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
def mostrar_resultados(df, consulta):
    """Muestra los resultados de la consulta seleccionada.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        consulta (str): Consulta seleccionada por el usuario.
    """
    if consulta == 'Mostrar las primeras 5 filas':
        st.write('Primeras 5 filas:')
        st.dataframe(df.head())
    elif consulta == 'Cantidad de filas y columnas':
        st.write('Dimensiones del DataFrame:')
        st.write(df.shape)
    elif consulta == 'Tipos de datos de cada columna':
        st.write('Tipos de datos:')
        st.write(df.dtypes)
    elif consulta == 'Mostrar columnas con valores nulos':
        st.write('Valores nulos por columna:')
        st.write(df.isnull().sum())
    elif consulta == 'Resumen estadístico de las columnas numéricas':
        st.write('Resumen estadístico:')
        st.write(df.describe())
    elif consulta == 'Frecuencia de valores únicos para una columna':
        columna = st.selectbox('Selecciona una columna:', df.columns)
        if columna in df.select_dtypes(include=['object']).columns:
            st.write(f"Frecuencia de valores únicos para '{columna}':")
            st.bar_chart(df[columna].value_counts())
        else:
            st.warning(f"La columna '{columna}' no es categórica.")
    elif consulta == 'Visualizar distribución de una variable numérica':
        columna = st.selectbox('Selecciona una columna numérica:', df.select_dtypes(include=['number']).columns)
        fig, ax = plt.subplots()
        sns.histplot(data=df, x=columna, kde=True)
        st.pyplot(fig)

# Lista de opciones para el selectbox
consultas_seleccionadas = [
    "Selecciona una consulta",  # Opción predeterminada
    "Mostrar las primeras 5 filas",
    "Cantidad de filas y columnas",
    "Tipos de datos de cada columna",
    "Mostrar columnas con valores nulos",
    "Resumen estadístico de las columnas numéricas",
    "Frecuencia de valores únicos para una columna",
    "Visualizar distribución de una variable numérica"
]

# Crear el selectbox para elegir una opción
consulta = st.selectbox('Selecciona una consulta:', consultas_seleccionadas)

# Cargar el DataFrame con manejo de errores
try:
    df = pd.read_csv('./static/datasets/DataGYM.csv', sep=';')  # Usar el separador adecuado
    
    # Solo mostrar resultados si el usuario selecciona una opción válida
    if consulta != "Selecciona una consulta":
        mostrar_resultados(df, consulta)
    else:
        st.write("Por favor, selecciona una consulta para ver los resultados.")
except FileNotFoundError:
    st.error("El archivo CSV no fue encontrado. Verifica la ruta.")
except pd.errors.EmptyDataError:
    st.error("El archivo CSV está vacío.")
except Exception as e:
    st.error(f"Ha ocurrido un error: {e}")



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



    




