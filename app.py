import streamlit as st

st.title("Conversor de temperatura")
celsius = st.number_input("VGrados Celsius")
fahrenheit = celsius * 9 / 5 + 32
st.write(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
