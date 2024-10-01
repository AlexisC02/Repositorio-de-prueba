import random
import string

class Password:
    def __init__(self, longitud=8, contrasenia=None):
        self.__longitud = longitud
        self.__contrasenia = contrasenia

    def genContrasenia(self):
        rangMin = 10**(self.__longitud-1)
        rangMax = (10**self.__longitud)-1
        
        gen_contra = random.randint(rangMin, rangMax)
        return print(f"contrasenia: {gen_contra}")

    def __str__(self):
        return f"Longitud: {self.__longitud}, Contrasenia: {self.__contrasenia}"
    
####################################################    

contrasenia1 = Password()
contrasenia2 = Password(8)

print(contrasenia1)
print(contrasenia2)

contrasenia2.genContrasenia()