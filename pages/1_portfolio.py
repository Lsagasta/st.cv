import streamlit as st
import utilidades as ut


st.set_page_config(page_title="Lucas Sagasta - Data Analyst", page_icon="📊", layout="centered")


def main():

    # Importo Estilos CSS
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


# ------------- INTRO ---------------
    st.header("Portfolio", divider="rainbow")
    st.write("")
    st.markdown("""

**Aquí te comparto algunas de las soluciones de visualización de datos y automatización de reportes que he desarrollado.**
\n**Todos los proyectos fueron desarrollados en colaboración con el cliente, asegurando que cada etapa del proceso reflejara sus requerimientos específicos. Desde la planificación inicial hasta la implementación final, se tuvo en cuenta cada detalle proporcionado por el cliente, ajustando la solución a medida que surgían nuevas necesidades o propuestas de mejora.**
\n **¡Te invito a ver más detalles de cada uno de mis trabajos!**
""")
    
    

    st.write("")
    st.divider()

# SEGUIMIENTOS DE VISITAS
# Titulo:
    st.markdown(''' ### **Solución integral de visualización de datos para empresa proveedora de telas** ''')


    st.write("")
# Descripción:
    st.markdown("""
##### Resumen:            
Este tablero de control fue diseñado para una empresa proveedora de telas, permitiendo gestionar y monitorear de forma eficiente las visitas a clientes, el avance de objetivos comerciales y la autorización de ventas.
##### Indicadores clave:
* **Seguimiento de visitas a clientes**: Control detallado de las visitas realizadas a clientes, mostrando información relevante como fechas, frecuencia de visitas, y estado de cumplimiento.
* **Seguimiento de cumplimiento de objetivos**: Monitoreo del avance hacia los objetivos comerciales, incluyendo métricas de ventas y autorizaciones.
* **Automatización de reportes**: Generación automática de reportes para vendedores y gerencia, facilitando el acceso a información actualizada y relevante.
* **Integración de fuentes de datos**: Consolidación de todas las fuentes de datos (ventas, visitas, muestras, finanzas) en un solo lugar para una visión completa y precisa.
* **Diseño adaptable a dispositivos**: Cada tablero ha sido optimizado según el dispositivo donde será consultado: móviles, PCs o videowalls, asegurando una experiencia de usuario eficiente y adaptada a las necesidades operativas.
""")
# Imagenes:
    colA, colB, colC = st.columns([5, 5, 5], vertical_alignment="top")
    with colA:
        st.image("imgs/bt1.png")
    with colB:
        st.image("imgs/bt2.png")
        st.write("")
    with colC:
        st.image("imgs/bt3.png")
# Tags:
    mensaje = st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <span class="tag-verde">Looker</span>
                    <span class="tag-verde">Google Apps Script</span>
                    <span class="tag-verde">Big query</span>
                    <span class="tag-verde">SQL</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
# Botón de detalle:
    colA, colB, colC = st.columns([5, 10, 5], vertical_alignment="top")
    with colB:
        if st.button("Ver más sobre este proyecto", icon=":material/search:", use_container_width=True, type="primary"):
            st.switch_page("pages/2_bt.py")
# -----------FIN PROYECTO---------------
    st.divider()


# CALL CENTER
# Titulo:
    st.markdown(''' ### **Monitoreo: Centro de Atención Telefónica** ''')

    
    st.write("")

    st.write("")

    st.markdown("""##### Resumen:
                \nTablero de control diseñado para el Centro de Atención Telefónica del **Ministerio de Educación**, permitiendo el monitoreo del desempeño tanto del área como de cada agente.
                \nA través de este sistema, se pueden gestionar de manera eficiente las incidencias de los programas **Conectar Igualdad** y **Conectividad Nacional**, asegurando un alto nivel de eficiencia operativa y atención a los usuarios.
##### Indicadores clave:
* **Cantidad de Llamadas Atendidas:** Número total de llamadas atendidas durante el día.
* **Tiempo Promedio de Espera Antes de Abandonar:** Tiempo promedio que los usuarios esperaron antes de colgar.
* **Horas Habladas por Agente:** Tiempo total en el que los agentes estuvieron en llamadas, medido por cada agente.
* **Cantidad de Agentes Activos:** Número de agentes que estuvieron atendiendo llamadas en un periodo específico.
* **Reintentos de Llamadas Perdidas:** Indicador que muestra cuántas llamadas perdidas fueron atendidas en un intento posterior.
""")
                


# Imagenes:
    colA, colB, colC = st.columns([5, 5, 5], vertical_alignment="top")
    with colA:
        st.image("imgs/cat3.png")
    with colB:
        st.image("imgs/cat1.png")
        st.write("")
    with colC:
        st.image("imgs/cat2.png")



    # Tags:
    st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <span class="tag-salmon">Python</span>
                    <span class="tag-salmon">Grafana</span>
                    <span class="tag-salmon">Apache E-charts</span>
                    <span class="tag-salmon">SQL</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
# Botón de detalle:
    colA, colB, colC = st.columns([5, 10, 5], vertical_alignment="top")
    with colB:
        if st.button("Ver más sobre este proyecto", icon=":material/search:", use_container_width=True, type="primary", key=2):
            st.switch_page("pages/4_cat.py")
# -----------FIN PROYECTO----------------
    st.divider()



# CALL CENTER
# Titulo:
    st.markdown(''' ### **Conectar Igualdad 2021 - 2023** ''')


    # Descripción:
    st.markdown("""
                    ##### Resumen:
                    \nEste tablero muestra el avance de los programas Conectar Igualdad y Conectividad Nacional entre 2021 y 2023. 
                    \nSu propósito es monitorear el estado de entrega de netbooks y el estado de conectividad en las instituciones educativas. 
                    \nTambién ofrece información sobre el tipo de equipamiento entegado/instalado.
                
                \n##### Indicadores clave:
                \n* **Netbooks Entregadas 2021-2023:** Total de netbooks entregadas durante el período, diferenciando entre áreas urbanas y rurales.
                \n* **Escuelas Alcanzadas 2023:** Cantidad de escuelas que han recibido netbooks, con clasificación por zonas urbanas, rurales y EIB (Educación Intercultural Bilingüe).
                \n* **Conectividad Escolar:** Número de escuelas conectadas a internet a través del programa.
                \n* **Escuelas en Proceso Logístico:** Número de escuelas pendientes de recibir netbooks o instalación de conectividad.
                \n* **Stock Disponible:** Cantidad de netbooks disponibles en stock para futuras distribuciones.
                                



                                """)
# Imagenes:
    colA, colB, colC = st.columns([5, 5, 5], vertical_alignment="top")
    with colA:
        st.image("imgs/ci1.png")
    with colB:
        st.image("imgs/ci3.png")
        st.write("")
    with colC:
        st.image("imgs/ci2.png")

# Tags:
    st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <b>Tecnologías: </b>
                    <span class="tag-celeste">Looker</span>
                    <span class="tag-celeste">Google Apps Script</span>
                    <span class="tag-celeste">Python</span>
                    <span class="tag-celeste">Google Sheets</span>
                    <span class="tag-celeste">SQL</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    st.write("")
    st.write("")
# Botón de detalle:
    colA, colB, colC = st.columns([5, 10, 5], vertical_alignment="top")
    with colB:
        if st.button("Ver más sobre este proyecto", icon=":material/search:", use_container_width=True, type="primary", key=3):
            st.switch_page("pages/5_ci.py")
# -----------FIN PROYECTO----------------
    st.divider()


# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
