import streamlit as st

st.set_page_config(page_title = "Lucas Sagasta",page_icon = "📊")

def main():
    # Importo Estilos CSS
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    
    # ----------- SIDEBAR -------------

    st.sidebar.image("imgs/perfilLS.png", width=180)
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
# ----------- /SIDEBAR/ -------------

    st.write("BT")

    st.image("imgs/bt4.png")



# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()