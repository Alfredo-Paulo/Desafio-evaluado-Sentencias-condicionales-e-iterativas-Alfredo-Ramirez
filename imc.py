def calcular_imc(peso_kg, altura_cm):
    altura_m = altura_cm / 100 
    imc = peso_kg / (altura_m ** 2) 
    return round(imc, 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"

def main():
    peso = float(input("Ingrese su peso en Kg: "))
    altura = float(input("Ingrese su altura en centímetros: "))

    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print("Su IMC es:", imc)
    print("Según la OMS, usted tiene:", clasificacion)

if __name__ == "__main__":
    main()