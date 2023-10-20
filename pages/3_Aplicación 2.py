import streamlit as st

# Título de la aplicación
st.title("Aplicación de Saludo")

# Entrada de texto para el nombre del usuario
nombre = st.text_input("Ingresa tu nombre:")

# Botón para generar el saludo
if st.button("Generar Saludo"):
    if nombre:
        st.write(f"Hola, {nombre}! ¡Bienvenido a tu aplicación de Streamlit!")
    else:
        st.write("Por favor, ingresa tu nombre para generar un saludo.")
