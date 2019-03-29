def imprimir_primeros_dos(cadena):
    print(cadena[:2])

def imprimir_ultimos_tres(cadena):
    print(cadena[-3:])

def imprimir_cada_dos(cadena):
    print(cadena[::2])

def imprimir_inverso(cadena):
    print(cadena[::-1])

def imprimir_original_e_inverso(cadena):
    print(cadena + cadena[::-1])

imprimir_ultimos_tres("hola")

imprimir_cada_dos("recta")

imprimir_inverso("hola mundo!")

imprimir_original_e_inverso("reflejo")
