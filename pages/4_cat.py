import streamlit as st
import utilidades as ut

st.set_page_config(page_title="Lucas Sagasta", page_icon="📊", layout="centered")


def main():
    with open('styles.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# ----------- SIDEBAR -------------
    st.sidebar.image("imgs/perfilLS.png", use_column_width=True)
    # st.sidebar.write(
    # '"Encuentro soluciones efectivas en el análisis de datos mediante herramientas accesibles y eficientes."')
    ut.generarMenu()
        #Cargar el archivo PDF (asegúrate de que esté en el directorio correcto)
    with open("imgs/Lucas S. Data Analyst.pdf", "rb") as file:
        pdf_data = file.read()
    # Crear el botón de descarga para el PDF
    st.sidebar.download_button(
        type="primary",
        label="📄 Descarga mi CV",
        data=pdf_data,
        file_name="lucas-sagasta-cv.pdf",
        mime="application/pdf",
        use_container_width= True,
    )
# ----------- /SIDEBAR/ -------------

    st.header("Centro de Atención Telefónica")
    st.subheader("Conectar Igualdad - Conectividad Escolar")
    st.write("Este tablero presenta el análisis diario de las llamadas gestionadas por el Centro de Atención Telefónica, proporcionando una visión detallada del rendimiento del equipo y las métricas clave del servicio.")

    st.image("imgs/cat3.png")
    st.markdown("""


### 1. Resumen de Llamadas

- **Atendidas**
- **Salientes**
- **Abandonadas**
- **% de Abandonadas**
- **Horas Habladas**
- **Cantidad de Agentes**

### 2. Contestado/Abandonado por Fecha

Gráfico de barras que representa la cantidad de llamadas atendidas y abandonadas para cada fecha analizada (del 6/05 al 15/05). Cada barra verde muestra las llamadas atendidas y las amarillas las llamadas abandonadas.

### 3. % por Tipo de Llamado

Un gráfico de pastel que desglosa el porcentaje de llamadas:
- **Atendidas**: 90% del total.
- **Salientes**: 7%.
- **Perdidas**: 2%.

### 4. Tiempo de Espera antes de Abandonar

Gráfico de barras verticales que muestra la distribución del tiempo de espera de las llamadas que fueron abandonadas. El rango de mayor abandono es entre 00:00 y 00:59 segundos de espera, con 67 llamadas abandonadas.
""")
    st.image("imgs/cat2.png")
    st.markdown("""


### 5. Resumen por Agente

Tabla que detalla el desempeño de cada agente:

- **Agente**: Nombre del agente.
- **Atendidas**: Número de llamadas atendidas por el agente.
- **Hablando**: Tiempo total hablado.
- **Salientes**: Número de llamadas salientes realizadas por el agente.
- **Hablando S**: Tiempo total hablado en llamadas salientes.

### 6. Atendidas & Tiempo Hablado

Gráfico de barras y línea que combina la cantidad de llamadas atendidas por cada agente con el tiempo total hablado. Las barras representan las llamadas atendidas y la línea azul muestra el tiempo hablado.

### 7. Resumen de Llamadas Atendidas en Rangos de 10 Minutos

Gráfico de barras que muestra la distribución de las llamadas atendidas en intervalos de 10 minutos a lo largo del día, proporcionando información sobre los momentos de mayor carga de trabajo.

    """)
    st.image("imgs/cat1.png")
    st.markdown("""


### 8. Resumen de Llamadas Abandonadas en Rangos de 10 Minutos

Gráfico de barras que refleja las llamadas abandonadas por los usuarios, distribuidas en intervalos de 10 minutos durante el día, identificando los momentos de mayor abandono.

### 9. Seguimiento de Llamadas Perdidas

Tabla que detalla las llamadas perdidas, incluyendo:
- **ID**: Identificador de la llamada.
- **Q de llamadas**: Cantidad de llamadas realizadas por ese número.
- **Fue Atendida Posteriormente**: Si la llamada fue atendida en intentos posteriores.
- **Tiempo de Espera antes de Abandonar**: Tiempo que esperó antes de que la llamada fuese abandonada.
""")

    
   


# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
