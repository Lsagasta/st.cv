import streamlit as st


st.set_page_config(page_title="Lucas Sagasta - Data Analyst",
                   page_icon="📊", layout="wide")


def main():

    # Estilos CSS
    with open('styles.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.sidebar.image("imgs/perfilLS.png", width=150)
    st.sidebar.write(
        '"Encuentro soluciones efectivas en el análisis de datos mediante herramientas accesibles y eficientes."')
    # Cargar el archivo PDF (asegúrate de que esté en el directorio correcto)
    with open("imgs/Lucas S. Data Analyst.pdf", "rb") as file:
        pdf_data = file.read()

    # Crear el botón de descarga para el PDF
    st.sidebar.download_button(
        type="secondary",
        label="📄 Descarga mi CV",
        data=pdf_data,
        file_name="lucas-sagasta-cv.pdf",
        mime="application/pdf",
    )

    st.header(" Lucas Sagasta", divider="rainbow")
    st.subheader(
        "Analista de Datos - Científico de Datos - Especialista en IA")

    st.write("")

    st.write("📊 Soy un analista de datos especializado en el seguimiento de operaciones, ventas y logística.")
    st.write("💡 A lo largo de mi carrera, he diseñado soluciones de integración de datos y visualización de indicadores utilizando diversas plataformas y tecnologías, como SQL, Python, LookerStudio, Power BI, y Excel, para diferentes sectores industriales.")
    st.write("🛠️ Tengo experiencia en la recolección y procesamiento de datos, disposición, creación de dashboards, y automatización de reportes diarios vía correo electrónico.")
    st.write("🚀 He participado en proyectos clave que han impulsado la toma de decisiones estratégicas dentro de las organizaciones.")
    st.write("🌟 Soy un profesional comprometido con la mejora continua y la innovación, siempre en busca de nuevas formas de aprovechar los datos para generar valor y ventajas competitivas.")

    st.write("")

    st.subheader("Herramientas y Tecnologías:")

    st.markdown("""
<div>
    <span class="tag-python">Python</span>
    <span class="tag-powerbi">Power BI</span>
    <span class="tag-looker">Looker</span>
    <span class="tag-sql">SQL</span>
    <span class="tag-appscript">Apps Script</span>
    <span class="tag-grafana">Grafana</span>
    <span class="tag-Echarts">Apache Echarts</span>
</div>
""", unsafe_allow_html=True)

    st.write("")

    st.write("")

    st.write("")

    st.header("Algunos de mis trabajos", divider="rainbow")
    st.write("")


# PRIMER FILA DE TRABAJOS
    colA, colB = st.columns([4, 4])
# SEGUIMIENTOS DE VISITAS
    with colA:
        st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')
        st.markdown("""
<div>
    <span class="tag-python">Python</span>
    <span class="tag-powerbi">Power BI</span>
    <span class="tag-looker">Looker</span>

</div>
""", unsafe_allow_html=True)

        st.write("")

        col1, col3 = st.columns([3, 4])

        with col3:
            st.image("imgs/seguimiento1.jpg")

        with col1:
            st.markdown("""


Este **tablero para móviles** tiene como objetivo ayudar a los **vendedores** de una distribuidora de **telas denim** a:""")

        st.markdown("""- Monitorear visitas a clientes.
- Alcanzar sus metas de ventas mensuales.""")

        if st.button("Ver mas sobre este proyecto"):
            st.switch_page("pages/2_bt.py")


# MONITOREO LLAMADAS

    with colB:

        st.markdown(''' ### **Monitoreo: Centro de Atención Telefónica** ''')

        col1, col3 = st.columns([3, 4])

        with col3:
            st.image("imgs/call1.png")

        with col1:
            st.markdown("""
        Este **tablero de control** fue creado para ayudar al **Centro de Atención Telefónica del Ministerio de Educación de la Nación**, que gestiona incidencias de los programas **Conectar Igualdad** y **Conectividad Nacional**, a:""")
        st.markdown(""" 
        - Monitorear el desempeño del área y de cada agente.
        - Identificar áreas de mejora.
        - Asegurar una operación eficiente.""")
        if st.button("Ver mas sobre este proyecto", key=1):
            st.switch_page("pages/1_cat.py")

    # SEGUNDA FILA DE TRABAJOS

    colA, colB = st.columns([4, 4])
# CONIG
    with colA:
        st.markdown(''' ### **Conectar Igualdad 2021-2023** ''')

        col1, col3 = st.columns([3, 4])

        with col3:
            st.image("imgs/conig.png")

        with col1:
            st.markdown("""


Tablero que tiene como objetivo mostrar el avance de los programas **Conectar Igualdad** y el **Programa de Conectividad Nacional** durante el periodo comprendido entre 2021 y 2023.
""")
        st.markdown("""
- Monitoreo de estado de la entrega de Netbooks
- Monitoreo del estado de conectividad y tipo de equipamiento instalado.""")

        if st.button("Ver mas sobre este proyecto", key=2):
            st.switch_page("pages/2_bt.py")
# TABLERO 4
    with colB:

        st.markdown(''' ### **Monitoreo: Centro de Atención Telefónica** ''')

        col1, col3 = st.columns([3, 4])

        with col3:
            st.image("imgs/psl.png")

        with col1:
            st.markdown("""
        Este **tablero de control** fue creado para ayudar al **Centro de Atención Telefónica del Ministerio de Educación de la Nación**, que gestiona incidencias de los programas **Conectar Igualdad** y **Conectividad Nacional**, a:
        """)
        st.markdown("""
        - Monitorear el desempeño del área y de cada agente.
        - Identificar áreas de mejora.
        - Asegurar una operación eficiente.""")

        if st.button("Ver mas sobre este proyecto", key=3):
            st.switch_page("pages/1_cat.py")


# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
