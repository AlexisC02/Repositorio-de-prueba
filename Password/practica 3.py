import random
import string

class Prueba:
    def __init__(self, longitud=0, contrasenia=None):
        self.__longitud = longitud
        self.__contrasenia = contrasenia

    def genCont(self, longitud):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        #contrasenia = "".join(random.choice(caracteres)) for _ in range(self.__longitud) 
        #return contrasenia   