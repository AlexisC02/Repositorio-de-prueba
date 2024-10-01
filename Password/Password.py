import random
import string

class Password:
    def __init__(self, longitud=8, contrasenia=None):
        self.longitud = longitud
        self.contrasenia = contrasenia

    def Generador(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        self.contrasenia = ''.join(random.choice(caracteres) for i in range(self.longitud))
        return self.contrasenia 

    def esFuerte(self):
        may = sum(1 for c in self.contrasenia if c.isupper())
        min = sum(1 for c in self.contrasenia if c.islower())
        num = sum(1 for c in self.contrasenia if c.isdigit())
        sim = sum(1 for c in self.contrasenia if c in string.punctuation)
        if may>2 and min>1 and num>5:
            return print(True)
        else:
            return print(False)
    
    def __str__(self):
        return f"Longitud: {self.longitud}, Contraseña: {self.contrasenia}"
    
#----------------------------------------------------------------    

contrasenia1 = Password() 
contrasenia2 = Password(longitud=30)

contrasenia2.Generador()
#contrasenia2.esFuerte()

#----------------------------------------------------------------

print(contrasenia1)
print(contrasenia2)

#print(contrasenia2.contrasenia)

contrasenia2.esFuerte()