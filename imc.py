def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
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
    
def entrada_valida(valor_str, tipo):
    try:
        valor = float(valor_str)
        if tipo == "peso":
            if valor < 10 or valor > 300:
                raise ValueError("El peso debe estar entre 10 kg y 300 kg.")
        elif tipo == "altura":
            if valor < 0.5 or valor > 2.5:
                raise ValueError("La altura debe estar entre 0.5 m y 2.5 m.")
        return valor
    except ValueError as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    print("Calculadora de IMC")
    peso = entrada_valida(input("Ingresa tu peso en kg: "), "peso")
    altura = entrada_valida(input("Ingresa tu altura en metros: "), "altura")
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")
    print(f"Interpretación: {interpretar_imc(imc)}")
