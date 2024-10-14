import streamlit as st
import utilidades as ut


st.set_page_config(page_title="Lucas Sagasta - Data Analyst", page_icon="📊")


def main():

    # Importo Estilos CSS
    with open('styles.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------- SIDEBAR -------------

    st.sidebar.image("imgs/perfilLS.png", use_column_width=True)
    # st.sidebar.write(
    # '"Encuentro soluciones efectivas en el análisis de datos mediante herramientas accesibles y eficientes."')
    # Cargar el archivo PDF (asegúrate de que esté en el directorio correcto)
   # with open("imgs/Lucas S. Data Analyst.pdf", "rb") as file:
    #  pdf_data = file.read()

    # Crear el botón de descarga para el PDF
   # st.sidebar.download_button(
    #    type="secondary",
    #   label="📄 Descarga mi CV",
    #   data=pdf_data,
    #   file_name="lucas-sagasta-cv.pdf",
    #  mime="application/pdf",

  #  )
    ut.generarMenu()
# ----------- /SIDEBAR/ -------------


# ------------- INTRO ---------------
    st.header("Portfolio", divider="rainbow")
    st.write("")


# SEGUIMIENTOS DE VISITAS
# Titulo:
    st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')
# Tags:
    st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <b>Tecnologías: </b>
                    <span class="tag-python">Python</span>
                    <span class="tag-powerbi">Power BI</span>
                    <span class="tag-looker">Looker</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    st.write("")
# Descripción:
    st.markdown("""Tablero para móviles diseñado para ayudar a sus vendedores a mantenerse al día con las visitas a sus cartera de clientes y alcanzar sus metas de ventas mensuales. 
                """)
    st.markdown("""Tablero para móviles diseñado para ayudar a sus vendedores a mantenerse al día con las visitas a sus cartera de clientes y alcanzar sus metas de ventas mensuales. 
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
# Tags:
    st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <b>Tecnologías: </b>
                    <span class="tag-python">Python</span>
                    <span class="tag-powerbi">Power BI</span>
                    <span class="tag-looker">Looker</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    st.write("")
# Descripción:
    st.markdown("""
                    Este tablero de control fue diseñado para el Centro de Atención Telefónica del Ministerio de Educación, que gestiona incidencias de los programas Conectar Igualdad y Conectividad Nacional.
                    \nFacilita el monitoreo del desempeño tanto del área como de cada agente, permitiendo identificar áreas de mejora y asegurar la eficiencia operativa.
                    \nA través de un análisis detallado de métricas clave, ayuda a optimizar la gestión, mejorar la toma de decisiones y garantizar que el servicio mantenga altos estándares de calidad en la atención a los usuarios.
                    
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
# Botón de detalle:
    colA, colB, colC = st.columns([5, 10, 5], vertical_alignment="top")
    with colB:
        if st.button("Ver más sobre este proyecto", icon=":material/search:", use_container_width=True, type="primary", key=2):
            st.switch_page("pages/2_bt.py")
# -----------FIN PROYECTO----------------
    st.divider()


# CALL CENTER
# Titulo:
    st.markdown(''' ### **Conectar Igualdad 2021 - 2023** ''')
# Tags:
    st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <b>Tecnologías: </b>
                    <span class="tag-python">Python</span>
                    <span class="tag-powerbi">Power BI</span>
                    <span class="tag-looker">Looker</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    st.write("")
# Descripción:
    st.markdown("""
                    Este tablero de control muestra el avance de los programas Conectar Igualdad y Conectividad Nacional entre 2021 y 2023. 
                    \nSu propósito es monitorear el estado de entrega de netbooks y el estado de conectividad en las instituciones educativas. 
                    \nTambién ofrece información sobre el tipo de equipamiento instalado, permitiendo un seguimiento detallado del progreso de ambos programas y asegurando que se cumplan los objetivos de inclusión digital y mejora de la conectividad en todo el país.
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
# Botón de detalle:
    colA, colB, colC = st.columns([5, 10, 5], vertical_alignment="top")
    with colB:
        if st.button("Ver más sobre este proyecto", icon=":material/search:", use_container_width=True, type="primary", key=3):
            st.switch_page("pages/2_bt.py")
# -----------FIN PROYECTO----------------
    st.divider()


# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
