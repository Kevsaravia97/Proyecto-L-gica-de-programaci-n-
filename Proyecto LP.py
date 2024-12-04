# Código básico para el programa
import time
import os
import random

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

import os

# Dimensiones de la cuadrícula
Ancho = 20
Alto = 20

# Función para crear una cuadrícula vacía
def crear_cuadricula():
    return [[" " for _ in range(Ancho)] for _ in range(Alto)]

# Función para mostrar la cuadrícula
def mostrar_cuadricula(cuadricula):
    os.system("cls" if os.name == "nt" else "clear")
    for fila in cuadricula:
        print("|" + "".join(fila) + "|")
    print("=" * (Ancho + 2))

# Función para dibujar la serpiente en la cuadrícula
def dibujar_serpiente(cuadricula, serpiente):
    for x, y in serpiente:
        if 0 <= x < Alto and 0 <= y < Ancho:
            cuadricula[x][y] = "O"
        else:
            print(f"Advertencia: La coordenada ({x}, {y}) está fuera de los límites.")

# Generar comida1
def generar_comida(cuadricula, serpiente):
    while True:
        x = random.randint(0, Alto - 1)
        y = random.randint(0, Ancho - 1)
        if (x, y) not in serpiente:
            cuadricula[x][y] = "x"
            return (x, y)


# Función para mover la serpiente
def mover_serpiente(serpiente, direccion):
    cabeza = serpiente[0]
    if direccion == "w":  # Arriba
        nueva_cabeza = (cabeza[0] - 1, cabeza[1])
    elif direccion == "s":  # Abajo
        nueva_cabeza = (cabeza[0] + 1, cabeza[1])
    elif direccion == "a":  # Izquierda
        nueva_cabeza = (cabeza[0], cabeza[1] - 1)
    elif direccion == "d":  # Derecha
        nueva_cabeza = (cabeza[0], cabeza[1] + 1)
    serpiente.insert(0, nueva_cabeza)  # Agregar nueva cabeza
    serpiente.pop()  # Remover la cola

# Función para verificar colisiones
def verificar_colision(serpiente):
    cabeza = serpiente[0]
    # Colisión con paredes
    if cabeza[0] < 0 or cabeza[0] >= Alto or cabeza[1] < 0 or cabeza[1] >= Ancho:
        return True
    # Colisión con su propio cuerpo
    if cabeza in serpiente[1:]:
        return True
    return False

# Inicialización del juego
serpiente = [(5, 5), (5, 4), (5, 3)]
direccion = "d"  # Dirección inicial (derecha)
cuadricula = crear_cuadricula()
comida = generar_comida(cuadricula, serpiente)

# Coordenadas iniciales de la serpiente
serpiente = [(5, 5), (5, 4), (5, 3)]

# Inicialización del juego
cuadricula = crear_cuadricula()
dibujar_serpiente(cuadricula, serpiente)
mostrar_cuadricula(cuadricula)  # ¡Se pasa la cuadrícula aquí!
