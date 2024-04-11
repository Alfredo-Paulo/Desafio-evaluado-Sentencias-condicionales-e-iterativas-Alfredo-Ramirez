clave_valida = "1234"
intentos_maximos = 3
intentos = 0

while intentos < intentos_maximos:
    clave_ingresada = input("Ingrese su clave: ")
    if clave_ingresada == clave_valida:
        print("Bienvenid@ al servicio")
        break
    else:
        intentos += 1
        if intentos == intentos_maximos:
            print("Tarjeta retenida")
        else:
            print("Clave incorrecta. Inténtelo de nuevo.")