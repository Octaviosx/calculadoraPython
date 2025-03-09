def suma_avanzada(numeros):
    i = 0
    resultado = 0
    while i < numeros:
        a = int(input("Ingresa un numero: "))
        resultado = resultado + a
        i += 1
    print(f"El resultado de la suma es: {resultado}")
