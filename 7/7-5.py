def es_primo(numero):
    '''Recibe un numero natural y devuelve si es primo'''
    if numero == 1:
        return False
    for i in range(2, numero//2 + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(numeros):
    '''Recibe una lista de numeros naturales
    Y devuele una lista con los que son primos'''
    primos = []
    for numero in numeros:
        if es_primo(numero):
            primos.append(numero)

    return primos

def factorial(numero):
    fact = 1
    for i in range(1, numero+1):
        fact *= i

    return fact

def lista_factorial(numeros):
    '''Recibe una lista de numeros naturales
      Y devuelve una lista de sus factoriales'''
    resultado = []
    for numero in numeros:
        resultado.append(factorial(numero))

    return resultado


lista = [1,2,3,4,5,6,7,8,9,10]
print(lista_factorial(lista))



























'''
def es_primo(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False

    return True

def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(2,n+1):
        fact *= i
    
    return fact

'''
'''
numeros = range(1,20)
numeros_primos = list(filter(es_primo,numeros))
numeros_factorial = list(map(factorial,numeros))

print ("Primos del 1 al 20:\n",numeros_primos)
print ("\nFactorial del 1 al 20:\n",numeros_factorial)
'''
