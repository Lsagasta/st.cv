import streamlit as st

def main():

    st.sidebar.image("imgs/lucas.png", use_column_width=True)
    st.sidebar.write('"Encuentro soluciones efectivas en el análisis de datos mediante herramientas accesibles y eficientes."')



   
    st.header(" Lucas Sagasta", divider="rainbow")
    st.subheader("Analista de Datos - Científico de Datos - Especialista en IA")
    
    
    st.write("")
  
    st.write("📊 Soy un analista de datos especializado en el seguimiento de operaciones, ventas y logística.")
    st.write("💡 A lo largo de mi carrera, he diseñado soluciones de integración de datos y visualización de indicadores utilizando diversas plataformas y tecnologías, como SQL, Python, LookerStudio, Power BI, y Excel, para diferentes sectores industriales.")
    st.write("🛠️ Tengo experiencia en la recolección y procesamiento de datos, disposición, creación de dashboards, y automatización de reportes diarios vía correo electrónico.")
    st.write("🚀 He participado en proyectos clave que han impulsado la toma de decisiones estratégicas dentro de las organizaciones.")
    st.write("🌟 Soy un profesional comprometido con la mejora continua y la innovación, siempre en busca de nuevas formas de aprovechar los datos para generar valor y ventajas competitivas.")

    st.write("")


    # Cargar el archivo PDF (asegúrate de que esté en el directorio correcto)
    with open("imgs/Lucas S. Data Analyst.pdf", "rb") as file:
        pdf_data = file.read()

    # Crear el botón de descarga para el PDF
    st.download_button(
        label="Descarga mi CV",
        data=pdf_data,
        file_name="lucas-sagasta-cv.pdf",
        mime="application/pdf",
    )
    


    st.write("")


    st.write("")

    st.header("Algunos de mis trabajos", divider="rainbow")  
    st.write("")

    st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')

    col1,col3 = st.columns([3,4])

    with col3:
        st.image("imgs/seguimiento1.jpg")

  

    with col1:
        st.markdown("""


Este **tablero para móviles** tiene como objetivo ayudar a los **vendedores** de una distribuidora de **telas denim** a:

- Monitorear visitas a clientes.
- Alcanzar sus metas de ventas mensuales.""")
        

    expander = st.expander("Ver mas sobre este proyecto")

    expander.markdown("""
Cada vendedor tiene establecido que debe realizar una visita a cada uno de sus clientes según la categoría del mismo. Los resultados de esta implementación son:

- **Ayuda a la planificación de rutas**.
- **Optimización del tiempo** en la rutina de visitas.
- **Fortalecimiento de la relación** con los clientes.
- **Identificación de nuevas oportunidades de venta** y respuesta a las necesidades emergentes.

Desde gerencia, se pudo evaluar el rendimiento de cada vendedor, optimizando la gestión de la cartera de clientes, priorizando a los más importantes y asegurando que se les dedique suficiente tiempo y recursos.
""")
    

    col3,col1 = expander.columns([2,4])

    with col3:
        st.image("imgs/seguimiento2.jpg")

  

    with col1:
        st.markdown("""
### Proceso

1. **Creación de Base de Datos**: El primer paso fue crear una base de datos en **Google Sheets** que estableciera la relación entre los vendedores y los clientes. Esta lista se actualiza semanalmente mediante una consulta SQL desde Google Sheets a la base de datos de la empresa.
  
2. **Integración de Visitas**: Luego, se integran las visitas realizadas en esta base. Para ello, se utilizó un conector hacia la API de la aplicación empleada por los vendedores para registrar las visitas y pedidos de los clientes.
  
3. **Construcción de la Base Consolidada**: Mediante un script, se construye una base consolidada que contiene toda la información necesaria para la construcción de los tableros.
  
4. **Creación de Tableros**: Se construyeron ocho tableros, uno para cada vendedor, y se otorgaron los permisos correspondientes, asegurando que solo el propio vendedor y los supervisores puedan visualizar su cartera.
  
5. **Reporte Automático**: Finalmente, se implementó un reporte automático que envía un correo con el resumen del día al cierre de la jornada laboral.

""")
        
    st.write("")

    st.markdown(''' ### **Tablero de Control para Centro de Atención Telefónica** ''')

    col1, col3 = st.columns([3, 4])

    with col3:
        st.image("imgs/call1.png")

    with col1:
        st.markdown("""
    Este **tablero de control** fue creado para ayudar al **Centro de Atención Telefónica del Ministerio de Educación de la Nación**, que gestiona incidencias de los programas **Conectar Igualdad** y **Conectividad Nacional**, a:

    - Monitorear el desempeño del área y de cada agente.
    - Identificar áreas de mejora.
    - Asegurar una operación eficiente.""")
            
    expander = st.expander("Ver más sobre este proyecto")

    expander.markdown("""
    ### Información mostrada en el tablero:
    1. **Cantidad de llamadas:**
    - Llamadas atendidas, salientes y perdidas.
    2. **Porcentaje de llamadas atendidas** sobre el total.
    3. **Horas habladas** entre todos los agentes.
    4. **Cantidad de agentes conectados**.
    5. **Análisis del tiempo de espera** de los usuarios antes de colgar.
    6. **Desempeño detallado de cada agente**: llamadas contestadas y tiempo hablado.
    7. **Informe de llamadas atendidas** en intervalos de 10 minutos.
    8. **Informe de llamadas abandonadas** en intervalos de 10 minutos.
    9. **Análisis de números no atendidos** y su seguimiento en llamadas sucesivas.

    El tablero optimiza la gestión de recursos, mejora la experiencia del usuario y reconoce el desempeño de los agentes.
    """)

    col3, col1 = expander.columns([2, 4])

    with col3:
        st.image("imgs/call2.png")

    with col1:
        st.markdown("""
    ### Proceso

    1. **Limpieza de datos**: Los informes crudos recibidos del sistema **3CX** se procesaron en **Python**.
    2. **Subida a SQL**: Los datos se almacenaron en una base de datos **SQL**.
    3. **Visualización**: Se crearon gráficos en **Grafana** y con la biblioteca **Apache Echarts**.
    4. **Automatización**: El tablero se actualiza con datos en tiempo real, proporcionando métricas clave.

    ### Resultado

    Este tablero permitió monitorear el desempeño del centro en tiempo real, mejorando la eficiencia operativa y motivando a los agentes al contar con un sistema transparente y de reconocimiento.
    """)
    expander.image("imgs/call3.png")


    

    


        
 


    





# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()