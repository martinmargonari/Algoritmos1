def reemplazar_digitos(cadena):
    cadena_sin_digitos = cadena[0];
    for i in range(1,len(cadena)):
        if (cadena[i - 1] == " " or cadena[i - 1].isdigit()) and cadena[i].isdigit():
            cadena_sin_digitos += 'X'
        else:
            cadena_sin_digitos += cadena[i]

    return cadena_sin_digitos

print(reemplazar_digitos("Nota de Algoritmos1: 10"))
