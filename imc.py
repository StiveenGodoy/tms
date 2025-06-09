import math
import streamlit as st

def calcular_imc(peso, altura):
    imc = peso / math.pow(altura, 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    st.title("Calculadora de IMC")
    st.write("Esta herramienta te permite calcular tu Índice de Masa Corporal (IMC).")

    # Entradas con validación automática
    peso = st.number_input("Ingresa tu peso en kg:", min_value=10.0, max_value=300.0, step=0.1)
    altura = st.number_input("Ingresa tu altura en metros:", min_value=0.5, max_value=2.5, step=0.01)

    if st.button("Calcular IMC"):
        imc = calcular_imc(peso, altura)
        st.success(f"Tu IMC calculado es: {imc:.2f}")
        st.info(f"Interpretación: {interpretar_imc(imc)}")

if __name__ == "__main__":
    main()
