def mcd(m,n):
    '''Obtener maximo comun divisor entre dos numeros n y m
       Mediante el algortimo de Euclides
    '''
    if m < n:
        return mcd(n,m)

    r = m % n
    if r == 0:
        return n

    return mcd(n,r)

assert(mcd(15,9)) == 3
assert(mcd(9,15)) == 3
assert(mcd(10,8)) == 2
assert(mcd(12,6)) == 6
