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

    st.header(" Lucas Sebastián Sagasta", divider="rainbow")
    st.subheader(
        "Analista de Datos - Científico de Datos - Especialista en IA")

    st.write("")

    st.write("📊 Soy un analista de datos especializado en el seguimiento de operaciones, ventas y logística.")
    st.write("💡 A lo largo de mi carrera, he diseñado soluciones de integración de datos y visualización de indicadores utilizando diversas plataformas y tecnologías, como SQL, Python, LookerStudio, Power BI, y Excel, para diferentes sectores industriales.")
    st.write("🛠️ Tengo experiencia en la recolección y procesamiento de datos, disposición, creación de dashboards, y automatización de reportes diarios vía correo electrónico.")
    st.write("🚀 He participado en proyectos clave que han impulsado la toma de decisiones estratégicas dentro de las organizaciones.")
    st.write("🌟 Soy un profesional comprometido con la mejora continua y la innovación, siempre en busca de nuevas formas de aprovechar los datos para generar valor y ventajas competitivas.")
    st.write("")
    st.write("")

    st.header("Algunos de mis trabajos", divider="rainbow")
    st.write("Mira algunos de mi tableros realizados:")

    col1, col2, col3, col4 = st.columns([5, 5, 5, 5])
    with col1:
        st.image("imgs/bt3.png")
    with col2:
        st.image("imgs/cat1.png")
    with col3:
        st.image("imgs/ci3.png")
    with col4:
        st.image("imgs/cat3.png")

    col5, col6, col7, col8 = st.columns([5, 5, 5, 5])
    with col5:
        st.image("imgs/bt1.png")
    with col6:
        st.image("imgs/cat2.png")
    with col7:
        st.image("imgs/ci2.png")
    with col8:
        st.image("imgs/ci1.png")

    if st.button("Ver portfolio completo", icon=":material/search:", use_container_width=True, type="primary"):
        st.switch_page("pages/1_portfolio.py")

    st.write("")
    st.write("")

    st.header("Proyectos", divider="rainbow")
    st.write("Mirá algunos de mis proyectos personales y academicos")

    st.write("")
    st.write("")

    st.header("Tecnologías con las que trabajo", divider="rainbow")
    st.write("")

    col1, col2, col3, col4, col5, col6 = st.columns([5, 5, 5, 5, 5, 5])
    with col1:
        st.image("imgs/python.png")
    with col2:
        st.image("imgs/looker.png")
    with col3:
        st.image("imgs/apscripst.png")
    with col4:
        st.image("imgs/grafana.png")
    with col5:
        st.image("imgs/powerbi.png")
    with col6:
        st.image("imgs/sql.png")


# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
