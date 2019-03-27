import random

def adivinar_numero(numero):
    numero_usr = int(input("Ingrese número: "))
    if numero_usr == numero:
        return True
    if numero_usr > numero:
        print("El número ingresado es mayor")
        return False
    print("El número ingresado es menor")
    return False

print("\nBienvenido al juego de adivinador de numeros\n")
limite = int(input("Ingrese el límite del numero a adivinar (entre 0 y..): "))
numero_secreto = random.randrange(limite)

while not adivinar_numero(numero_secreto):
    print("Intente nuevamente\n")

print("Número adivinado!")
