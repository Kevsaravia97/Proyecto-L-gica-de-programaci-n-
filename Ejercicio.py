"""a = 10
b = 15

print("¿a es igual a b?", a == b)"""




"""a = int(input("Ingrese valor de a: "))
b = int(input("Ingrese valor de b: "))

print(f"Has ingresado a = {a} y b = {b}")

print("¿a es igual a b?", a == b)

print("¿a es distinto que b", a != b) 

print("a es mayor que b", a > b)

print("a es menor que b", a < b)

print("a es mayor o igual que", a >=b)"""

"""a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))

print(f"Has ingresado a = {a} y b = {b}")

print("¿a es igual a b?", a == b)

print("¿a es distinto que b", a != b) 

print("a es mayor que b", a > b)

print("a es menor que b", a < b)

print("a es mayor o igual que", a >=b)"""

"""num1 = True
nume2 = False"""

"""edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingreso sus ingresos: "))

a = edad>18
b = ingresos>3000

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingreso sus ingresos: "))

print("Eres adulto y tienes bueos ingresos", {a and b})
print("Eres adulto o tienes buenos ingresos", {a or b}"""

"""if edad > 18:
    edad_mayor = edad
    print("Edad válida almacenada: {edad_mayor}")

if ingresos > 3.000:
    ingresos_mayor = ingresos
    print("Ingreoss válidos almacenados: {ingreos_mayor}")

if edad"""

"""nume1 = int(input("Ingrese el número: "))

if nume1 > 0:
    print("El número es positivo.")

elif nume1 < 0:
    print("El número es negativo.")

else:
    print("El número es cero")"""


"""x = 10

if x > 5:
    print("x es mayor que 5.")
elif x == 5:
    print("x es igual a 5.")
else:
    print("x es menor que 5.")"""

"""edad = int(input("Ingrese su edad: "))

if edad >= 65:
    print("Eres adulto mayor")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")"""

"""edad = input("Ingresa tu edad: ")
print("Eres genial")"""

"""calif = float(input("Ingrese calificación: "))

if calif >= 9:
    print("Excelente")
elif calif >= 7 and calif < 9:
    print("Aprobado")
elif calif >= 5 and calif < 7:
    print("Necesita tutorias")
elif calif >= 1 and calif < 4:
    print("Requiere tutoría")
else:
    print("Reprobado")"""

"""calif = float(input("Ingrese calificación: "))

if 0 <= calif <= 10:
    if calif >= 9:
        print("Excelente")
    elif calif >= 7 and calif < 9:
        print("Aprobado")
    elif calif >= 5 and calif < 7:
        print("Necesita tutorias")
    elif calif >= 1 and calif < 4:
        print("Requiere tutoría")
    else:
        print("Reprobado")
else:
    print("El valor debe ser entre 0 y 10")"""

"""Votación = float(input("Ingrese la letra de la lista (m, e, j, i, a):: "))
if votación in ["m", "e", "j", "i", "a"]:
    print(f"Voto registrado correctamente: ")
else:
    print("Entrada inválida. Por favor, ingrese una letra válida (m, e, j, i, a).")"""

"""print("Menú de opciones")
print("a. Saludar")
print("b. Despedirse")
print("c. Salir")

opción = input("Ingresa una opción: ")
if opción=="a":
    print("Saludar")
elif opción=="b":
    print("Despedirse")
elif opción=="c":
    print("Adios")
else: 
    print("Opción incorrecta")"""

"""x = 5 

if x > 10: 

    print("x es mayor que 10") 

else: 

    print("x es menor o igual que 10")"""


"""x = 15 

if x > 10: 

    print("x es mayor que 10") 

elif x > 5: 

    print("x es mayor que 5") 

else: 

    print("x es menor o igual que 5")"""

"""a = 0 
b = 0
while a < 10:
    a += 1
    print(a)"""

"""a = 1
pares = 0
while a <= 20:
    if a % 2 == 0:
        pares += 1
    a += 1
print("Existen", pares, "números pares entre 1 y 20.")"""

"""contador = 0
while contador < 10:
    contador += 1
    print(contador)"""

"""número = 1
while número < 11:
    número += 1
    print(número)"""


"""numero = float(input("Ingrese un número: "))
resultado = numero
while resultado <= 10:
    print("Resultado actual: {resultado}")
    resultado *= numero  # Multiplicar el resultado por el número ingresado
print("El resultado final {resultado} supera 10.")"""

"""num = int(input("Ingrese un número: "))
contador = 1
while contador < 11:
    resultado = num * contador
    print(f"{num} * {contador} = {resultado}")
    contador += 1"""

"""suma = 0
for i in range(1, 101):
    suma += i
print("La suma de los números del 1 al 100 es:", suma)"""

for i in range(20) :
    print(i)
