suma = 0

while True:
    numero = int(input("Ingrese un número entero (-1 para terminar): "))
    if numero == -1:
        break
    suma += numero

print("La suma de los números ingresados es:", suma)