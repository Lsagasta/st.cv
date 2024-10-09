import streamlit as st

st.set_page_config(page_title = "Lucas Sagasta",page_icon = "📊", layout="wide")

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


    st.markdown("""
        <div class="flex-container">
            <!-- Sección de etiquetas alineadas a la izquierda -->
            <div>
                <span class="tag-python">Python</span>
                <span class="tag-powerbi">Power BI</span>
                <span class="tag-looker">Looker</span>
            </div>
            <!-- Botón alineado a la derecha -->
            <div>
                <button class="custom-button">Ver más sobre este proyecto 🚀</button>
            </div>
        </div>
    """, unsafe_allow_html=True)






# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()