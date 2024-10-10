import streamlit as st


st.set_page_config(page_title="Lucas Sagasta - Data Analyst",page_icon="📊")


def main():



    # Importo Estilos CSS
    with open('styles.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------- SIDEBAR -------------

    st.sidebar.image("imgs/perfilLS.png", use_column_width = True)
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

    st.header("Proyectos", divider="rainbow")
    st.write("")


# SEGUIMIENTOS DE VISITAS

    st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')



# SEGUIMIENTOS DE VISITAS

    st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <b>Técnologías: </b>
                    <span class="tag-python">Python</span>
                    <span class="tag-powerbi">Power BI</span>
                    <span class="tag-looker">Looker</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    
    st.write("")

    

    



    st.markdown("""Tablero para móviles diseñado para ayudar a sus vendedores a mantenerse al día con las visitas a sus cartera de clientes y alcanzar sus metas de ventas mensuales. 
                """)
    st.markdown("""Tablero para móviles diseñado para ayudar a sus vendedores a mantenerse al día con las visitas a sus cartera de clientes y alcanzar sus metas de ventas mensuales. 
                """)    

    
    colA, colB, colC = st.columns([5,5,5],vertical_alignment="top")
# SEGUIMIENTOS DE VISITAS
    with colA:
        st.image("imgs/seguimiento1.jpg")

    with colB:
        st.image("imgs/seguimiento1.jpg")
        st.write("")

    with colC:
        st.image("imgs/seguimiento1.jpg")




    colA, colB, colC = st.columns([5,10,5],vertical_alignment="top")
    with colB:
        if st.button("▶️       Ver más",use_container_width = True ,type="primary"):
            st.switch_page("pages/2_bt.py")

    st.divider()

    # SEGUIMIENTOS DE VISITAS

    st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')


    # SEGUIMIENTOS DE VISITAS

    st.markdown("""
                <!-- Sección de etiquetas alineadas a la izquierda -->
                <div>
                    <b>Técnologías: </b>
                    <span class="tag-python">Python</span>
                    <span class="tag-powerbi">Power BI</span>
                    <span class="tag-looker">Looker</span>
                </div>
                </div>
        """, unsafe_allow_html=True)
    
    st.write("")

    

    



    st.markdown("""Tablero para móviles diseñado para ayudar a sus vendedores a mantenerse al día con las visitas a sus cartera de clientes y alcanzar sus metas de ventas mensuales. 
                """)
    st.markdown("""Tablero para móviles diseñado para ayudar a sus vendedores a mantenerse al día con las visitas a sus cartera de clientes y alcanzar sus metas de ventas mensuales. 
                """)    

    
    colA, colB, colC = st.columns([5,5,5],vertical_alignment="top")
# SEGUIMIENTOS DE VISITAS
    with colA:
        st.image("imgs/seguimiento1.jpg")

    with colB:
        st.image("imgs/seguimiento1.jpg")
        st.write("")

    with colC:
        st.image("imgs/seguimiento1.jpg")




    colA, colB, colC = st.columns([5,10,5],vertical_alignment="top")
    with colB:
        if st.button("▶️       Ver más",use_container_width = True ,type="primary",key = 5):
            st.switch_page("pages/2_bt.py")

    st.divider()
    


















    



        
        






        
    





# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
