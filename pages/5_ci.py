import streamlit as st
import utilidades as ut

st.set_page_config(page_title="Lucas Sagasta", page_icon="📊", layout="wide")


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

    st.write("conig")

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


# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
