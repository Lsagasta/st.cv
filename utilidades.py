import streamlit as st


def generarMenu():
    with st.sidebar:
        st.page_link("app.py", label="Inicio", icon=":material/home:")
        st.page_link("pages/1_portfolio.py", label="Portfolio",
                     icon=":material/monitoring:")
