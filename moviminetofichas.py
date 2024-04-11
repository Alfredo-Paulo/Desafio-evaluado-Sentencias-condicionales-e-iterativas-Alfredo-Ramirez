def jugar_maquina():
    posicion_actual = 1  # La posición inicial es 1
    while posicion_actual != 4:  # Continuar hasta llegar a la posición final
        ficha = input("Ingrese una ficha (a, b, c, d) o presione 'n' para salir: ")
        if ficha == 'n':
            if posicion_actual == 4:
                print("¡Ganaste!")
            else:
                print("¡Perdiste!")
            break
        elif ficha == 'a':
            posicion_actual += 1
        elif ficha == 'b':
            posicion_actual += 2
        elif ficha == 'c':
            posicion_actual -= 1
        elif ficha == 'd':
            posicion_actual -= 3
        if posicion_actual < 1:
            posicion_actual = 1  # No se puede ir más abajo de la posición 1
    else:
        print("¡Ganaste!")

jugar_maquina()