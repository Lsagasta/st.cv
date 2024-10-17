import streamlit as st
import utilidades as ut

st.set_page_config(page_title="Lucas Sagasta", page_icon="📊", layout="centered")


def main():
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

    st.header("Conectar Igualdad - Tablero de Comando")
    st.subheader("Conectar Igualdad - Conectividad Escolar")
    st.write("Este tablero monitorea el estado de las entregas de netbooks y el avance en la conectividad y matrícula alcanzada en el marco del programa Conectar Igualdad. El tablero está dividido en las siguientes secciones clave:")


    st.image("imgs/tablero_ci.png")
    st.markdown("""
## 1. NB Entregadas 2021 - 2023
- **Netbooks Entregadas:** Total de netbooks entregadas en los últimos años, diferenciadas entre áreas urbanas y rurales.
- **Netbooks en Proceso Logístico:** Cantidad de netbooks en proceso de distribución.

## 2. Escuelas Entregadas 2023
- **Escuelas Entregadas:** Número de escuelas a las que se ha entregado netbooks durante el año 2023, con una diferenciación entre urbanas, rurales y EIB (Educación Intercultural Bilingüe).
- **Escuelas en Proceso Logístico:** Cantidad de escuelas pendientes de recibir las entregas.

## 3. Matrícula Alcanzada
- **Matrícula Alcanzada:** Porcentaje y número de estudiantes alcanzados con el programa, diferenciados entre áreas urbanas y rurales (aglomerado, disperso, etc.).
- **Matrículas Validadas:** Cantidad de estudiantes con matrícula validada.

## 4. Escuelas Alcanzadas
- **Escuelas Alcanzadas:** Cantidad de escuelas donde se ha alcanzado la matrícula objetivo, con detalles para áreas urbanas y rurales.
- **Escuelas Validadas:** Escuelas con matrícula validada.

## 5. Redes Locales
- **Redes Locales (Instalaciones de Equipos WIFI):** Cantidad de escuelas con redes locales instaladas.
  
## 6. Conectividad
- **Conectividad (Servicios de Internet):** Número de escuelas conectadas a internet a través del programa.
- **Conectadas con Red Local:** Escuelas conectadas con equipos de red local (WIFI + Internet).

## 7. Conectividad Administrativa
- **Conectividad Administrativa:** Número de escuelas con servicios de conectividad para tareas administrativas.

## 8. Netbooks Entregadas 2021 - 2023 (Desglose por Provincia)
- **Desglose de Netbooks Entregadas:** Cantidad de netbooks entregadas por provincia entre 2021 y 2023.

## 9. Matrícula Alcanzada (Desglose por Provincia)
- **Desglose de Matrícula Alcanzada:** Porcentaje y cantidad de estudiantes alcanzados por provincia en el mismo período.

---
Este tablero proporciona una visión integral del estado de entrega de dispositivos, conectividad y alcance de la matrícula en las escuelas bajo el programa Conectar Igualdad.


""")
    st.image("imgs/tableroci2.png")
    st.markdown("""# Dirección de Programas - Distribución y Stock

Este tablero monitorea el estado de la distribución de netbooks y CUE (Centros Únicos Educativos) alcanzados a lo largo de los años del programa "Conectar Igualdad". Se desglosa por jurisdicción y brinda información sobre la logística y el stock disponible. Las secciones clave del tablero son:

## 1. Distribución por Año
- **CUE Alcanzados (2021 - 2023):** Cantidad de CUE alcanzados en los años 2021, 2022 y 2023, diferenciados por jurisdicción.
- **NB Entregadas (2021 - 2023):** Número de netbooks entregadas en cada año por provincia, mostrando un desglose por jurisdicción.
- **Total CUE Alcanzados y Total de NB Entregadas:** Suma total de CUE alcanzados y netbooks entregadas entre 2021 y 2023, para cada provincia.

## 2. Detalle por Ámbito
- **CUE Alcanzados (Urbano, Rural, EIB):** Detalle del número de CUE alcanzados por ámbito (urbano, rural, EIB) en los años 2021, 2022 y 2023, así como el total.
- **NB Entregadas (Urbano, Rural, EIB):** Detalle del número de netbooks entregadas por ámbito (urbano, rural, EIB) en los años 2021, 2022 y 2023, y el total.

## 3. Resumen de Logística
- **Netbooks en Proceso Logístico:** Cantidad de netbooks pendientes de distribución por jurisdicción.
- **Escuelas en Proceso Logístico:** Escuelas que están pendientes de recibir las netbooks por jurisdicción.
- **Matrículas Validadas y Escuelas Validadas:** Número de matrículas y escuelas que han validado el proceso de entrega de netbooks, desglosadas por provincia.

## 4. Indicadores de Stock y Logística
- **Stock Disponible:** Total de netbooks disponibles en stock para distribución.
- **Alta Técnica Aprobada:** Número de netbooks que han sido aprobadas técnicamente para ser entregadas.
- **Pendiente de Recepción:** Cantidad de netbooks que están pendientes de ser recibidas en los centros de distribución.
- **Netbooks a Ingresar:** Número de netbooks que aún están por ingresar al sistema de distribución (actualmente en cero).

---

Este tablero proporciona una visión clara del estado de distribución de netbooks y los avances en la conectividad a nivel jurisdiccional, así como el control de stock y logística para el programa Conectar Igualdad.

    """)
    st.image("imgs/ci3tablero.png")
    st.markdown("""


# Dirección de Programas - Conectividad

Este tablero monitorea el estado de conectividad de las escuelas y jurisdicciones dentro del programa "Conectar Igualdad". Proporciona un desglose de las escuelas conectadas, las que están pendientes, y el tipo de conectividad instalada. También incluye un análisis por jurisdicción y ámbito. Las principales secciones del tablero son:

## 1. Estado de Conectividad de Escuelas
- **Pendente, Alcanzado, Administrativo:** Muestra el estado de conectividad de las escuelas para cada jurisdicción, desglosado en tres categorías:
  - **Pendiente:** Escuelas que aún no han sido conectadas.
  - **Alcanzado:** Escuelas que ya tienen conectividad instalada.
  - **Administrativo:** Escuelas en proceso administrativo para la instalación.
  
## 2. Estado de Conectividad (Resumen)
- **CUEs alcanzados (Alcanzado Conectar Igualdad, Alcanzado Jurisdiccional, Pendiente):** 
  - Total de Centros Únicos Educativos (CUEs) conectados bajo el programa Conectar Igualdad y bajo programas jurisdiccionales.
  - Total de CUEs pendientes de recibir conectividad.
  - Número de **Alumnos** impactados por la conectividad.
  
## 3. Red Local - Estado de Conectividad
- **Instalado Conectar Igualdad, Instalado Jurisdiccional, Pendiente:** 
  - Total de CUEs con red local instalada bajo el programa.
  - Instalación jurisdiccional de redes locales.
  - CUEs pendientes de instalación de red local.
  - **Matrícula CUE:** Número de estudiantes matriculados en las escuelas conectadas según el tipo de instalación de red local.

## 4. Gráficos Circulares
- **Conectividad de Escuelas:** Muestra visualmente el porcentaje de CUEs con conectividad alcanzada, administrativa, y pendiente.
- **Red Local:** Representación visual del estado de instalación de redes locales en las escuelas, con categorías de instaladas (Conectar Igualdad y jurisdiccional), no aplicables, y pendientes.

---

Este tablero proporciona una visión integral del estado de conectividad de las escuelas bajo el programa "Conectar Igualdad", resaltando los avances y los puntos pendientes en cada jurisdicción, así como el impacto en la matrícula estudiantil.

""")



# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
