def calcular_salario():
    # Solicitar el número de empleados
    num_empleados = int(input("Ingrese el número de empleados: "))
    
    # Lista para almacenar los salarios de cada empleado
    salarios = []
    
    # Iterar sobre cada empleado
    for i in range(num_empleados):
        print(f"\nEmpleado {i+1}:")
        nombre = input("Ingrese el nombre del empleado: ")
        NHT = float(input("Ingrese el número de horas semanales trabajadas: "))
        VHC = float(input("Ingrese el valor de la hora trabajada: "))
        
        # Calcular el salario del empleado
        salario = NHT * VHC
        
        # Agregar el salario a la lista
        salarios.append((nombre, salario))
    
    # Imprimir los salarios de cada empleado
    print("\nSalarios a pagar:")
    for nombre, salario in salarios:
        print(f"{nombre}: ${salario}")

# Llamar a la función para iniciar el programa
calcular_salario()