import streamlit as st

st.title("Conversor de temperatura entre Celsius y Fahrenheit")

modo = st.radio("Convertir de:", [
                "Celsius a Fahrenheit", "Fahrenheit a Celsius"])
valor = st.number_input("Valor")

if modo == "Celsius a Fahrenheit":
    resultado = valor * 9 / 5 + 32
    st.success(f"**{round(resultado, 2)} °F**")
    st.caption(f"{valor} °C  Convertidos a fahrenheit")
else:
    resultado = (valor - 32) * 5 / 9
    st.success(f"**{round(resultado, 2)} °C**")
    st.caption(f"{valor} °F  Convertidos a celsius")
