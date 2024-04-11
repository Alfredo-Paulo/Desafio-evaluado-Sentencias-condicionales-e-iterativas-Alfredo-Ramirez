import random
import sys

def juego_cachipun(opcion_usuario):
    opciones_validas = ['piedra', 'papel', 'tijera']
    
    if opcion_usuario not in opciones_validas:
        print("Opción no válida. Las opciones válidas son: piedra, papel, tijera")
        return
    
    opcion_computadora = random.choice(opciones_validas)
    
    print("La computadora ha elegido:", opcion_computadora)
    
    if opcion_usuario == opcion_computadora:
        print("¡Empate!")
    elif (opcion_usuario == 'piedra' and opcion_computadora == 'tijera') or \
         (opcion_usuario == 'tijera' and opcion_computadora == 'papel') or \
         (opcion_usuario == 'papel' and opcion_computadora == 'piedra'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python cachipun.py [piedra/papel/tijera]")
    else:
        opcion_usuario = sys.argv[1].lower()
        juego_cachipun(opcion_usuario)