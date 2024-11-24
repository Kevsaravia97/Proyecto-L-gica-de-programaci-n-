# Código básico para el programa
import time
import os

# Menú de inciio
def menú_inicio() :
    print("<<<<< Bienvenido al Juego de la Serpiente>>>>>")
    print("1. Jugar")
    print("2. Reanudar")
    print("3. Salir")
    opción = input("Selecciona una opción, por favor: ")
    return opción.strip()

# Mostrar el menú
while True:
    opción = menú_inicio()
    if opción == "1":
        print("Iniciar el juego")
        break
    elif opción == "2":
        print("Reanudar partida")
        break
    elif opción == "3":
        print("Salir del juego")
        exit()
    else:
        print("Opción no válida. Intenta de nuevo")

# Dimensiones
Ancho = 20
Alto = 20

# Cuadricula
def crear_cuadricula():
    cuadricula = [["for _ in range (Ancho)"] for _ in range (Alto)]
    return cuadricula

def mostrar_cuadricula():
    os.system("cls" if os.name == "nt" else "clear")
    for fila in crear_cuadricula:
        print("|" + "" + "".join(fila) + "|")
    print("=" * (Ancho + 2))

# Posición inicial 
serpiente = [(5, 5), (5, 4), (5, 3)]

# Dibujar la serpiente en la cuadrícula
def dibujar_serpiente(cuadricula, serpiente):
    for x, y in serpiente:
        cuadricula[x][y] = "O"  # Representamos la serpiente con 'O'

