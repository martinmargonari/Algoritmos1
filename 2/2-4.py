def imprimir_pares(inicio, fin):
    for i in range(inicio - inicio % 2 + 2, fin, 2):
        print(i)

inicio = int(input("Ingrese numero inicial: "))
fin = int(input("Ingrese numero final: "))
imprimir_pares(inicio, fin)
