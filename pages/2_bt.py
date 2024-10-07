import streamlit as st

st.set_page_config(page_title = "Lucas Sagasta",page_icon = "📊", layout="wide")

def main():
    st.sidebar.image("imgs/perfilLS.png", use_column_width=True)
    st.sidebar.write('"Encuentro soluciones efectivas en el análisis de datos mediante herramientas accesibles y eficientes."')


    st.write("BT")



# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()