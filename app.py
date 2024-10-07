import streamlit as st

st.set_page_config(page_title = "Lucas Sagasta",page_icon = "📊", layout="wide")

def main():

    st.sidebar.image("imgs/perfilLS.png", use_column_width=True)
    st.sidebar.write('"Encuentro soluciones efectivas en el análisis de datos mediante herramientas accesibles y eficientes."')



   
    st.header(" Lucas Sagasta", divider="rainbow")
    st.subheader("Analista de Datos - Científico de Datos - Especialista en IA")
    
    
    st.write("")
  
    st.write("📊 Soy un analista de datos especializado en el seguimiento de operaciones, ventas y logística.")
    st.write("💡 A lo largo de mi carrera, he diseñado soluciones de integración de datos y visualización de indicadores utilizando diversas plataformas y tecnologías, como SQL, Python, LookerStudio, Power BI, y Excel, para diferentes sectores industriales.")
    st.write("🛠️ Tengo experiencia en la recolección y procesamiento de datos, disposición, creación de dashboards, y automatización de reportes diarios vía correo electrónico.")
    st.write("🚀 He participado en proyectos clave que han impulsado la toma de decisiones estratégicas dentro de las organizaciones.")
    st.write("🌟 Soy un profesional comprometido con la mejora continua y la innovación, siempre en busca de nuevas formas de aprovechar los datos para generar valor y ventajas competitivas.")

    st.write("")


    # Cargar el archivo PDF (asegúrate de que esté en el directorio correcto)
    with open("imgs/Lucas S. Data Analyst.pdf", "rb") as file:
        pdf_data = file.read()

    # Crear el botón de descarga para el PDF
    st.download_button(
        label="Descarga mi CV",
        data=pdf_data,
        file_name="lucas-sagasta-cv.pdf",
        mime="application/pdf",
    )
    


    st.write("")


    st.write("")

    st.header("Algunos de mis trabajos", divider="rainbow")  
    st.write("")


    colA,colB = st.columns([4,4])

    with colA:
        st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')

        col1,col3 = st.columns([3,4])

        with col3:
            st.image("imgs/seguimiento1.jpg")

  

        with col1:
            st.markdown("""


Este **tablero para móviles** tiene como objetivo ayudar a los **vendedores** de una distribuidora de **telas denim** a:

- Monitorear visitas a clientes.
- Alcanzar sus metas de ventas mensuales.""")
        

        if st.button("Ver mas sobre este proyecto"):
            st.switch_page("pages/2_bt.py")

        st.markdown("""
    <style>
        .tag-python {
            background-color: #306998;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-powerbi {
            background-color: #f2c811;
            color: black;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-looker {
            background-color: #4285f4;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-sql {
            background-color: #e34f26;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-appscript {
            background-color: #34a853;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-grafana {
            background-color: #f46800;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        
    </style>

    <div>
        <span class="tag-python">Python</span>
        <span class="tag-powerbi">Power BI</span>
        <span class="tag-looker">Looker</span>
        <span class="tag-sql">SQL</span>
        <span class="tag-appscript">Apps Script</span>
        <span class="tag-grafana">Grafana</span>

    </div>
    """, unsafe_allow_html=True)


    with colB:

        st.markdown(''' ### **Monitoreo: Centro de Atención Telefónica** ''')

        col1, col3 = st.columns([3, 4])

        with col3:
            st.image("imgs/call1.png")

        with col1:
            st.markdown("""
        Este **tablero de control** fue creado para ayudar al **Centro de Atención Telefónica del Ministerio de Educación de la Nación**, que gestiona incidencias de los programas **Conectar Igualdad** y **Conectividad Nacional**, a:

        - Monitorear el desempeño del área y de cada agente.
        - Identificar áreas de mejora.
        - Asegurar una operación eficiente.""")
            
        st.markdown("""
    <style>
        .tag-python {
            background-color: #306998;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-powerbi {
            background-color: #f2c811;
            color: black;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-looker {
            background-color: #4285f4;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-sql {
            background-color: #e34f26;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-appscript {
            background-color: #34a853;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        .tag-grafana {
            background-color: #f46800;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-right: 5px;
        }
        
    </style>

    <div>
        <span class="tag-python">Python</span>
        <span class="tag-powerbi">Power BI</span>
        <span class="tag-looker">Looker</span>
        <span class="tag-sql">SQL</span>
        <span class="tag-appscript">Apps Script</span>
        <span class="tag-grafana">Grafana</span>

    </div>
    """, unsafe_allow_html=True)

        if st.button("Ver mas sobre este proyecto", key = 1):
            st.switch_page("pages/1_cat.py")

        


    #--------------------------------

    colA,colB = st.columns([4,4])

    with colA:
        st.markdown(''' ### **Seguimiento de visitas para vendedores** ''')

        col1,col3 = st.columns([3,4])

        with col3:
            st.image("imgs/seguimiento1.jpg")

  

        with col1:
            st.markdown("""


Este **tablero para móviles** tiene como objetivo ayudar a los **vendedores** de una distribuidora de **telas denim** a:

- Monitorear visitas a clientes.
- Alcanzar sus metas de ventas mensuales.""")
        

        if st.button("Ver mas sobre este proyecto", key = 2):
            st.switch_page("pages/2_bt.py")


    with colB:

        st.markdown(''' ### **Monitoreo: Centro de Atención Telefónica** ''')

        col1, col3 = st.columns([3, 4])

        with col3:
            st.image("imgs/call1.png")

        with col1:
            st.markdown("""
        Este **tablero de control** fue creado para ayudar al **Centro de Atención Telefónica del Ministerio de Educación de la Nación**, que gestiona incidencias de los programas **Conectar Igualdad** y **Conectividad Nacional**, a:

        - Monitorear el desempeño del área y de cada agente.
        - Identificar áreas de mejora.
        - Asegurar una operación eficiente.""")

        if st.button("Ver mas sobre este proyecto", key = 3):
            st.switch_page("pages/1_cat.py")
        













# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()