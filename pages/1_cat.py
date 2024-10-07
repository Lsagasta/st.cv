import streamlit as st

st.set_page_config(page_title = "Lucas Sagasta",page_icon = "📊", layout="wide")

def main():
    st.sidebar.image("imgs/perfilLS.png", use_column_width=True)
    st.sidebar.write('"Encuentro soluciones efectivas en el análisis de datos mediante herramientas accesibles y eficientes."')

    st.write("cat")



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



# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()