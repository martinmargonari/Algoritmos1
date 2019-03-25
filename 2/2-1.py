def calcular_ganancia(dinero, interes, anios):
    return dinero * (1 + interes/100) ** anios

dinero = int(input("Ingrese capital inicial: "))
interes = int(input("Ingrese interes: "))
anios = int(input("Ingrese años: "))

print("El monto final será de: " + str(calcular_ganancia(dinero, interes, anios)))
