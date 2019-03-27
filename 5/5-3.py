import time

PASSWORD = "muyfacil"
LIMITE_INTENTOS = 3

def comparar_contrasenia(password, limite_intentos):
    ''' Funcion que compara una password con otra ingresada por el usuario.
        Con un máximo de <limite_intentos> intentos.
    '''
    for i in range(1, limite_intentos + 1):
        password_usuario = input("Ingrese una contraseña: ")
        if (password_usuario == password):
            return True
        print("Error. Le quedan", LIMITE_INTENTOS - i, "intentos\n")
        time.sleep(i)    
    return False

if comparar_contrasenia(PASSWORD, LIMITE_INTENTOS):
    print("\nBienvenido\n")
else:
    print("Error. Demasiados intentos")

