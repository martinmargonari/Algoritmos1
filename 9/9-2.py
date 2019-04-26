def contar_palabras(cadena):
    dict = {}
    palabras = cadena.split()
    
    for palabra in palabras:
        if not palabra.lower() in dict:
            dict[palabra.lower()] = 1
        else:
            dict[palabra.lower()] += 1

    return dict

def contar_caracteres(cadena):
    dict = {}
    for c in cadena:
        if not c.lower() in dict:
            dict[c.lower()] = 1
        else:
            dict[c.lower()] += 1

    return dict
        
cadena = 'Que lindo día que hace hoy'
print("CONTAR PALABRAS:")
print(contar_palabras(cadena))

print("\nCONTAR CARACTERES:")
print(contar_caracteres(cadena))
