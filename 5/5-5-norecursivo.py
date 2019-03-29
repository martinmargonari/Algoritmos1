def mcd(m,n):
    '''Obtener maximo comun divisor entre dos numeros n y m
       Mediante el algortimo de Euclides
    '''
    while m % n != 0:
        r = m % n
        m = n
        n = r
    
    return n

assert(mcd(15,9)) == 3
assert(mcd(9,15)) == 3
assert(mcd(10,8)) == 2
assert(mcd(12,6)) == 6
