from sumar import *
from resta import *
from multiplicacion import *
from dividir import *
from suma_avanzada import *

while True:
    print("""
          ***********************************************************************
          **************** Bienvenidos a calculadora en Python ******************
          ***********************************************************************""")
    operacion = int(input(
        '1) Sumar\n2) Restar\n3) Multiplicar\n4) Dividir\n5) Suma avanzada\n6) Salir\nIngresa la operación que deseas realizar: '))
    if operacion == 1:
        valor1 = int(input("Ingresa un numero: "))
        valor2 = int(input("Ingresa un numero: "))
        sumar(valor1, valor2)
    if operacion == 2:
        valor1 = int(input("Ingresa un numero: "))
        valor2 = int(input("Ingresa un numero: "))
        restar(valor1, valor2)
    if operacion == 3:
        valor1 = int(input("Ingresa un numero: "))
        valor2 = int(input("Ingresa un numero: "))
        multiplicar(valor1, valor2)
    if operacion == 4:
        valor1 = int(input("Ingresa un numero: "))
        valor2 = int(input("Ingresa un numero: "))
        divir(valor1, valor2)
    if operacion == 5:
        cantNumeros = int(
            input("Ingresa la cantidad de numeros que deseas sumar: "))
        suma_avanzada(cantNumeros)
    elif operacion == 6:
        break
    else:
        "Opción invalida, favor de ingresar una opción mostrada en el menú."
