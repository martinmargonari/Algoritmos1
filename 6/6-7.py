def comparar_cadenas(cadena_a, cadena_b):
    max_len = min(len(cadena_a), len(cadena_b))
   
    for i in range(max_len):
        if cadena_a[i] < cadena_b[i]:
            return cadena_a
        if cadena_b[i] < cadena_a[i]:
            return cadena_b

    if len(cadena_b) < len(cadena_a):
        return cadena_b

    return cadena_a

print(comparar_cadenas("kdanasfsafasd","kdaa"))
