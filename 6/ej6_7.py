def comparar_cadenas(cadena_a, cadena_b):
    ''' Devuelve la cadena que sea anterior en orden alfabético.
        En caso de ser iguales, devuelve la primera. '''
    max_len = min(len(cadena_a), len(cadena_b))
   
    for i in range(max_len):
        if cadena_a[i] < cadena_b[i]:
            return cadena_a
        if cadena_b[i] < cadena_a[i]:
            return cadena_b

    if len(cadena_b) < len(cadena_a):
        return cadena_b

    return cadena_a

def es_subcadena(cadena, subcadena):
    ''' Devuelve True si el segundo parametro es subcadena 
        del primero. De lo contrario devuelve False'''
    if len(cadena) < len(subcadena):
        return False

    for i in range(len(cadena)):
        es_sub = True
        for j in range(len(subcadena)):
            if cadena[i+j] != subcadena[j]:
                es_sub = False
                break
        if es_sub:
            return True

    return False

