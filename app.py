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

    st.header(" Lucas Sebastián Sagasta", divider="rainbow")
    st.subheader("Analista de Datos - Científico de Datos - Especialista en IA")

    st.write("")

    st.write("📊 Soy un analista de datos especializado en el seguimiento de operaciones, ventas y logística.")
    st.write("💡 A lo largo de mi carrera, he diseñado soluciones de integración de datos y visualización de indicadores utilizando diversas plataformas y tecnologías, como SQL, Python, LookerStudio, Power BI, y Excel, para diferentes sectores industriales.")
    st.write("🛠️ Tengo experiencia en la recolección y procesamiento de datos, disposición, creación de dashboards, y automatización de reportes diarios vía correo electrónico.")
    st.write(":robot_face: Actualmente me encuentro realizando investigaciones para implementar proyectos de Inteligencia Artificial en el ámbito educativo.")
    st.header("Experiencia", divider="rainbow")

    st.markdown("""**Educ.ar - Ministerio de Educación**:
        \n* Desarrollo de tableros de control y monitoreo en Power BI, Looker y Grafana.
        \n* Implementación de la automatización de informes diarios, coordinando la recopilación de datos de múltiples áreas.""")
    st.divider()
    st.markdown("""
        \n**Proyectos freelance:**        
        \n* Conexión y extracción de datos a través de APIs, automatización de procesos con Google Apps Script.
        \n* Creación de dashboards en Looker.
        \n* Automatización del envío de correos electrónicos personalizados con reportes de progreso diario y mensual.""")
        
    st.write("")

    st.header("Algunos de mis trabajos", divider="rainbow")
    st.write("**Una selección de mis tableros y automatizaciones realizadas estos últimos años:**")

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

   # st.header("Proyectos", divider="rainbow")
   # st.write("Mirá algunos de mis proyectos personales y academicos")

    st.write("")
    st.write("")

    st.header("Tecnologías con las que trabajo", divider="rainbow")
    st.write("")




        
    col1, col2, col3, col4, col5, col6 = st.columns([5, 5, 5, 5, 5, 5])
    with col1:
        st.image("imgs/python.png",width=50)
        st.markdown("""
                <div>
                    <span class="tag-crema">Python</span>
                </div>
                    """, unsafe_allow_html=True)
    with col2:
        st.image("imgs/looker.png",width=50)
        st.markdown("""
                <div>
                    <span class="tag-crema">Looker</span>
                </div>
                    """, unsafe_allow_html=True)
        
    with col3:
        st.image("imgs/apscripst.png",width=50)
        st.markdown("""
                <div>
                    <span class="tag-crema">Apps Scripts</span>
                </div>
                    """, unsafe_allow_html=True)
    with col4:
        st.image("imgs/grafana.png",width=50)
        st.markdown("""
                <div>
                    <span class="tag-crema">Grafana</span>
                </div>
                    """, unsafe_allow_html=True)
    with col5:
        st.image("imgs/powerbi.png",width=50)
        st.markdown("""
                <div>
                    <span class="tag-crema">Power BI</span>
                </div>
                    """, unsafe_allow_html=True)
    with col6:
        st.image("imgs/sql.png",width=50)
        st.markdown("""
                <div>
                    <span class="tag-crema">SQL Server</span>
                </div>
                    """, unsafe_allow_html=True)



# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
