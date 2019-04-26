def es_primo(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False

    return True

def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    
    return fact

numeros = range(1,20)
numeros_primos = list(filter(es_primo,numeros))
numeros_factorial = list(map(factorial,numeros))

print ("Primos del 1 al 20:\n",numeros_primos)
print ("\nFactorial del 1 al 20:\n",numeros_factorial)
