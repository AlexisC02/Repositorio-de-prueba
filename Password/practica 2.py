import secrets

class Prueba:
    def __init__(self, longitud=0, contasenia=None):
        self.__longitud = longitud
        self.__contrasenia = contasenia

    def generarContrasenia(self, longitud):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = ''.join(secrets.choice(alphabet) for i in range(self.__longitud))
        
        return password

contra_segura = Prueba(longitud=3)

print(contra_segura)