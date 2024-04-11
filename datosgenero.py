# Inicializar contadores para hombres, mujeres y no especificado, todos en cero.
contador_hombres = 0
contador_mujeres = 0
contador_no_especificado = 0
contador_total = 0

# Mientras el usuario no ingrese 'x':
while True:
    # Solicitar al usuario que ingrese el género ('m' para masculino, 'f' para femenino, 'n' para no especificado).
    genero = input("Ingrese el género (m para masculino, f para femenino, n para no especificado), o 'x' para terminar: ").lower()

    # Si el usuario ingresa 'x', terminar el bucle
    if genero == 'x':
        break

    # Incrementar el contador total en 1.
    contador_total += 1

    # Determinar el género y actualizar los contadores correspondientes
    if genero == 'm':
        contador_hombres += 1
    elif genero == 'f':
        contador_mujeres += 1
    elif genero == 'n':
        contador_no_especificado += 1
    else:
        print("Género no válido. Por favor, ingrese 'm', 'f' o 'n'.")

# Calcular los porcentajes de hombres, mujeres y no especificado
porcentaje_hombres = (contador_hombres / contador_total) * 100 if contador_total > 0 else 0
porcentaje_mujeres = (contador_mujeres / contador_total) * 100 if contador_total > 0 else 0
porcentaje_no_especificado = (contador_no_especificado / contador_total) * 100 if contador_total > 0 else 0

# Mostrar los porcentajes
print(f"Porcentaje de hombres: {porcentaje_hombres}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres}%")
print(f"Porcentaje de no especificado: {porcentaje_no_especificado}%")