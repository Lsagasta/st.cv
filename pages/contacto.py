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

    st.header("Contacto", divider="rainbow")

    contact_form = """
    <form action="https://submit-form.com/ZjCdiVVl0">
        <input type="text" id="name" name="name" placeholder="Nombre" required="" />
        <input type="email" id="email" name="email" placeholder="Email" required="" />
        <textarea
            id="message"
            name="message"
            placeholder="Mensaje"
            required=""
        ></textarea>
        <button type="submit">Enviar mensaje</button>
    </form>"""
    st.markdown(contact_form,  unsafe_allow_html=True)





# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
