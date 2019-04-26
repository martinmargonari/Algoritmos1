def tuplas_a_diccionario(tuplas):
    dict = {}
    for tupla in tuplas:
        if not tupla[0] in dict:
            dict[tupla[0]] = []
        dict[tupla[0]].append(tupla[1])

    return dict

l = [('Hola', 'don Pepito'), ('Hola','don Jose'), ('Buenos', 'días')]
print(tuplas_a_diccionario(l))
