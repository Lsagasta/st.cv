import streamlit as st


st.set_page_config(page_title="Lucas Sagasta - Data Analyst",page_icon="📊", layout="wide")


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

    st.write("")

    st.write("")

    st.header("Algunos de mis trabajos", divider="rainbow")
    st.write("")

# PRIMER FILA DE TRABAJOS
    colA, colB = st.columns([4, 4])
# SEGUIMIENTOS DE VISITAS
    with colA:
        st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')


        st.markdown("""Resúmen:
                    \nTablero para móviles diseñado para ayudar a sus vendedores a mantenerse al día con las visitas a sus cartera de clientes y alcanzar sus metas de ventas mensuales. 
                    \nEste tablero permite monitorear las visitas realizadas, sus objetivos de ventas, y visualizar de manera clara y sencilla su progreso hacia dichas metas. 
                    \nAdemás, el tablero integra información actualizada automáticamente, asegurando que los vendedores siempre tengan acceso a datos precisos y al día. 
                    \nLa iniciativa busca no solo optimizar la eficiencia operativa, sino también fortalecer las relaciones comerciales mediante una atención regular y oportuna con cada cliente.""")





        col1, col3 = st.columns([.5, .5],vertical_alignment="center")

        with col3:
            st.image("imgs/seguimiento1.jpg")
            

        with col1:
            st.markdown("""
                        **Resumen de Métricas/Indicadores**
                        
                        - Visita a clientes.
                        - Avance de objetivos.
                        - Detalle clientes.
                        - Ventas por proveedor
                        - Saldo de cuenta

                        """)
        
        
        

        col1, col3 = st.columns([4, 4],vertical_alignment="center")   
        with col1:
            st.markdown("""
            <!-- Sección de etiquetas alineadas a la izquierda -->
            <div>
                <span class="tag-python">Python</span>
                <span class="tag-powerbi">Power BI</span>
                <span class="tag-looker">Looker</span>
            </div>
            </div>
    """, unsafe_allow_html=True)
        
        with col3:
            if st.button("Ver mas sobre este proyecto 🚀"):
                st.switch_page("pages/2_bt.py")





# MONITOREO LLAMADAS

    with colB:

        st.markdown(''' ### **Monitoreo: Centro de Atención Telefónica** ''')
        st.write("")

        col1, col3 = st.columns([3, 4],vertical_alignment="top")

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


    st.divider()

    # SEGUNDA FILA DE TRABAJOS

    colA, colB = st.columns([4, 4])
# CONIG
    with colA:
        st.markdown(''' ### **Conectar Igualdad 2021-2023** ''')

        col1, col3 = st.columns([3, 4],vertical_alignment="top")

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

        col1, col3 = st.columns([3, 4],vertical_alignment="top")

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
