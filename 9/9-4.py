def oraciones_mas_largas(texto):
    oraciones = texto.split(".")
    dict = {}
    for oracion in oraciones:
        for letra in oracion:
            anterior = dict.get(letra.lower(), '')
            if len(anterior) < len(oracion):
                dict[letra.lower()] = oracion

    return dict

texto = "Hola, que tal. Hola como estas. Buenos dias. Muy buenos dias."
print(oraciones_mas_largas(texto))
