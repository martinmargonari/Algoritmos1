def suma_divisores(n):
    '''Devuelve la suma de todos los divisores de n
       sin incluirlo.'''

    suma = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            suma += i
            if  i != int(n/i):
                suma += int(n/i)

    return suma


def print_primeros_m_perfectos(m):
    print(1) #El 1 es un número perfecto

    encontrados = 1
    numero = 2

    while encontrados < m:
        if (suma_divisores(numero) == numero):
            encontrados += 1
            print(numero)
        numero += 1

def print_primeros_m_amigos(m):
    encontrados = 0
    numero = 2
    while encontrados < m:
        suma_divisores_n = suma_divisores(numero)
        suma_divisores_amigo = suma_divisores(suma_divisores_n)
        if suma_divisores_amigo == numero and suma_divisores_n > numero:
            encontrados += 1
            print("(",numero,",",suma_divisores_n,")")
        numero += 1
       

