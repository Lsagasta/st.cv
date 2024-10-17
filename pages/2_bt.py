import streamlit as st
import utilidades as ut
st.set_page_config(page_title="Lucas Sagasta", page_icon="📊", layout="centered")


def main():
    # Importo Estilos CSS
    with open("styles.css") as f:
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
    # SEGUIMIENTOS DE VISITAS
    # Titulo:
    st.header("Proveedor de telas DENIM", divider="blue")
    st.subheader("Tablero de visitas a clientes presenciales")
    st.write("Este tablero es un resumen visual del desempeño de visitas presenciales a clientes por parte de vendedores de telas. Los indicadores claves se dividen en tres secciones:")
    colA, colB = st.columns([5, 5], vertical_alignment="center")

    with colA:
        st.markdown("""



            **1. Visitas diarias y progreso:**
            - **Clientes visitados hoy:** Clientes visitados durante la jornada
            - **Avance:** % del objetivo comercial mensual alcanzado por vendedor hasta la fecha.
            - **Autorizado (metros):** Metros de tela autorizados para la venta por gerencia.
            - **Objetivo (metros):** Meta de venta mensual en metros de tela.

            **2. Clasificación de clientes por estado de vencimiento:**

            Se muestra la cantidad de clientes organizados en categorías **(A, B, C, D, E)** junto con cuántos de ellos están en estado vencido:

                    """)
    st.markdown("""



            **3. Estado detallado de visitas y vencimientos por cliente:**
            Cada fila de la tabla muestra la información de un cliente individual, incluyendo:

            - **Fantasia (Nombre del cliente):** El nombre o alias del cliente.
            - **Categoría (Cat):** Clasificación del cliente (A, B, C, D, E).
            - **Última visita:** Fecha en que fue visitado por última vez.
            - **Días vencidos:** Número de días desde que el cliente debía ser visitado (valores negativos indican que está dentro de la frecuencia de visita).
            - **Frecuencia de visita:** Número de días recomendados entre visitas (Dependiente de la clasificación del cliente).
            - **Visitas esperadas al mes:** Cuántas visitas se esperan al mes para ese cliente.
            - **Visitas del mes:** Número de visitas realizadas en el mes actual.

            **Leyenda de colores:**
            - **Rojo (Vencido):** El cliente no ha sido visitado en el tiempo previsto y está vencido.
            - **Naranja (Vence hoy):** El cliente debería ser visitado hoy.
            - **Amarillo (Vence mañana):** El cliente debería ser visitado mañana.
            - **Verde (OK):** El cliente está dentro del rango de visita esperado.

            **Este tablero permite hacer un seguimiento efectivo de las visitas a los clientes, asegurando que se mantenga el control sobre los vencimientos y el cumplimiento de los objetivos de ventas en metros de tela.**



""")

    with colB:
        st.image("imgs/bt4.png")

    st.subheader("Resumen del Detalle de Clientes")
    st.write("Este tablero muestra información detallada sobre las interacciones recientes con un cliente, incluyendo visitas, cortes y ventas. Los indicadores se dividen en tres secciones principales:")

    colC, colD = st.columns([5, 5], vertical_alignment="center")

    with colC:
        st.markdown("""

**1. Últimas Visitas**

Esta sección muestra las visitas recientes realizadas al cliente, incluyendo la fecha, tipo de muestra, artículo y estado del resultado.


**2. Cortes**
Esta sección lista los cortes entregados al cliente como muestra de producto, con la fecha, tipo de muestra, artículo y resultado.

**3. Últimas Ventas**
Aquí se detalla el historial reciente de ventas, incluyendo la fantasía (nombre del cliente), la fecha de venta, número de artículo, nombre del artículo, valor por metro y metros autorizados.



""")
    with colD:
        st.image("imgs/bt5.png")
    st.markdown(""" **Este tablero proporciona un resumen detallado de las interacciones recientes con el cliente, abarcando visitas, muestras enviadas para evaluación y ventas recientes.** """)

    st.subheader("Resumen del Saldo de Cuenta")
    st.write("Este tablero muestra un resumen del saldo de cuenta de la cartera de clientes del vendedor, con detalles sobre la deuda, capacidad de pago, depósitos pendientes y autorización de metros. Además, ofrece una tabla con el estado de las diferentes fantasías asociadas a la cuenta.")

    colE, colF = st.columns([5, 5], vertical_alignment="center")

    with colE:
        st.markdown("""
    **Indicadores Principales**

- **Deuda a la Fecha** 
- **Capacidad de Pago Mensual**
- **Depósitos Pendientes** 
- **Metros Autorizados** 
- **Valor Autorizado**
- **Metros no Autorizados**
- **Pagos últimos 30/60/90/120 días**
                    """)

    st.write("Este tablero proporciona una vista clara del estado financiero de la clienta, con énfasis en la deuda acumulada y los pagos realizados a lo largo de diferentes periodos.")

    with colF:
        st.image("imgs/bt6.png")

    st.subheader("Resumen de Visitas y Muestras Ofrecidas")
    st.write("Este tablero muestra un análisis detallado de las visitas realizadas por los vendedores, las muestras ofrecidas y las ventas concretadas entre el **1 de marzo de 2023 y el 15 de marzo de 2023**. Proporciona información sobre los tipos de clientes visitados, el desempeño por vendedor, y los resultados de las muestras ofrecidas.")

    colG, colH, colI = st.columns([5, 20, 5])

    with colH:
        st.image("imgs/bt3.png")

    st.markdown("""
## Indicadores Principales

- **Visitas Totales:** Muestra el número total de visitas realizadas, con una comparación porcentual respecto a un periodo anterior.
- **Clientes Visitados:** Refleja el número de clientes visitados y su variación porcentual.
- **Muestras Ofrecidas:** Número total de muestras ofrecidas, con un desglose por tipo de artículo (prenda).
- **Visitas sin Muestra:** Indica la cantidad de visitas realizadas donde no se ofreció ninguna muestra.
  
## Secciones de la Tabla

### Clientes Visitados

Esta tabla detalla el tipo de clientes visitados y la relación entre las visitas y los clientes.

- **Tipo de Cliente:** Agrupa a los clientes por categorías, como 'A', 'B', 'C', 'D', entre otros.
- **Visitas:** Muestra el número total de visitas realizadas por tipo de cliente.
- **Clientes Visitados:** Indica cuántos clientes fueron efectivamente visitados en cada categoría.
- **Visitas/Clientes:** Proporción de visitas por cliente en cada categoría.

### Visitas por Vendedor

Esta sección muestra un desglose por vendedor, destacando el número de visitas realizadas y los resultados de ventas.

- **Vendedor:** Nombre del vendedor.
- **Visitas:** Cantidad total de visitas realizadas por cada vendedor.
- **Clientes que Compraron:** Cantidad de clientes que compraron tras la visita.
- **Artículos Vendidos:** Número de artículos vendidos por cada vendedor.

### Ventas Concretadas

Muestra los productos vendidos durante el periodo, con el número de ventas de cada artículo.

- **Artículo:** Nombre o código del artículo vendido.
- **Ventas Concretadas:** Número total de ventas de cada artículo.

### Motivo de la Visita

Un gráfico circular que desglosa los motivos de las visitas realizadas:

- **Venta, Cobranzas, Entregas, Reclamo:** Tipos de motivo que originaron las visitas.

### Tipo de Encuentro

Otro gráfico circular que muestra cómo se llevaron a cabo los encuentros:

- **Visitado, Telefónica, Otros:** Métodos de contacto utilizados en las visitas.

### Resultado de la Muestra Ofrecida

Detalla las razones del resultado de las muestras ofrecidas:

- **Lo está evaluando, No le gusta, No tiene caja, Ya tiene tela, No cerró por precio:** Categorías que agrupan los resultados de las muestras ofrecidas a los clientes.

Este tablero ofrece una visión completa de la interacción entre los vendedores y los clientes, ayudando a identificar oportunidades de mejora en el proceso de ventas y seguimiento de muestras.
""")

    st.subheader("Cierre Diario de Operaciones")
    st.write("Este tablero proporciona un resumen del avance de cobranza por semana y el desempeño de los vendedores, con detalles sobre visitas, pedidos y conversiones. También incluye un análisis del resultado de las visitas.")

    colJ, colK = st.columns([5, 5])

    with colJ:
        st.markdown("""## Avance de Cobranza por Semana

Este indicador muestra el avance semanal de las cobranzas en porcentaje y valor real, comparado con el valor estimado:

- **Semana 1:** Avance de cobranza con el 100% de cumplimiento.
- **Semana 2:** Avance de cobranza con el 105.47% de cumplimiento.
- **Semana 3:** Avance de cobranza con el 110.82% de cumplimiento.
- **Semana 4:** Avance de cobranza del 77.23%, por debajo del estimado.
  
El avance total hasta el momento se encuentra en un **96.86%**, con una diferencia de -3.14% respecto al estimado.

## Detalle por Vendedor

Desglose de las actividades realizadas por los vendedores:

- **Visitas:** Cantidad total de visitas realizadas por cada vendedor.
- **Llamados:** Número de llamados realizados por los vendedores.
- **Pedidos:** Cantidad de pedidos generados.
- **Autorizado:** Monto total de dinero autorizado por cada vendedor.
- **Conversión:** Porcentaje de conversión de las visitas a pedidos.

## Resultado de la Visita (Por Prenda)

Este gráfico muestra las razones de los resultados de las visitas, agrupados en diferentes categorías:

- **Lo está evaluando:** Clientes que están evaluando las muestras ofrecidas.
- **No le gusta/Otros:** Razones generales por las cuales no les gustó el producto o se rechazó.
- **No cerró por precio:** Visitas que no finalizaron en ventas debido al precio.
- **Venta concretada:** Visitas que resultaron en una venta efectiva.
- **Ya tiene tela:** Clientes que ya disponían del material solicitado.
- **No tiene caja:** Razones financieras que impidieron la venta.
- **No cerró por plazo:** La venta no se concretó debido a los tiempos de entrega.
- **No está cortando:** El cliente no está en fase de producción.
- **Visita sin prenda:** Visitas en las que no se ofrecieron muestras.
""")

    with colK:
        st.image("imgs/bt7.png")


# ------------------------------------
# EJECUTAR MAIN
# ------------------------------------
# Ejecutar la función main cuando se carga la aplicación
if __name__ == "__main__":
    main()
