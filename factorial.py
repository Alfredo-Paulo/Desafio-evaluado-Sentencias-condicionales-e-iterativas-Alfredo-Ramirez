def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Calcular y mostrar el factorial del número ingresado
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")