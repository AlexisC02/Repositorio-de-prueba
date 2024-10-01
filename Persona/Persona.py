import random

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None, sexo=None, peso=00, altura=000):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = self.__generarDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
    
    def calcularIMC(self):
        if self.__peso == 0 or self.__altura == 0:
            print("Los valores en 0 no puden calcularse")
        else:    
            pesoIdeal = self.__peso/((self.__altura/100)**2)
            if pesoIdeal<20:
                return print(-1)
            elif pesoIdeal>=20 and pesoIdeal<=20 and pesoIdeal<=25:
                return print(0)
            elif pesoIdeal>25:
                return print(1)
        
    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return print(True)
        else:
            return print(False)

    def comprobarSexo(self):
        if self.__sexo == "M" or "F":
            return print(True)
        else:
            self.__sexo = "M"
            return print("La persona no posee un sexo contemplado")
        
    def set_nombre(self, nombre=None):
        self.__nombre = nombre

    def set_edad(self, edad=0):
        self.__edad = edad

    def set_sexo(self, sexo=None):
        self.__sexo = sexo

    def set_peso(self, peso=0):
        self.__peso = peso

    def set_altura(self, altura=0):
        self.__altura = altura               
    
    def __generarDNI(self):
        dni_gen = random.randint(10000000, 99999999)
        return dni_gen
        
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}, Sexo: {self.__sexo}, Peso: {self.__peso}, Altura: {self.__altura}"
    
    
    
persona1 = Persona()
persona2 = Persona(nombre="Diego", edad=45, sexo="M")
persona3 = Persona("Rodrigo", 24, 45673892, "M", 90, 178)

print(persona1)
print(persona2)
print(persona3)

persona3.calcularIMC()
persona3.esMayorDeEdad()
persona3.comprobarSexo()
#persona3.set_nombre(nombre="Gustavo")

#-------------------------------------------------------------------------------

nombreInp = input("Nombre ")
edadInp = int(input("Edad "))
sexoInp = input("Sexo ")
pesoInp = int(input("Peso "))
alturaInp = int(input("Altura "))

persona4 = Persona(nombre=nombreInp, edad=edadInp, sexo=sexoInp, peso=pesoInp, altura=alturaInp)
persona5 = Persona(nombre=nombreInp, edad=edadInp, sexo=sexoInp)
persona6 = Persona()

persona6.set_nombre()
persona6.set_edad()
persona6.set_sexo()
persona6.set_peso()
persona6.set_altura()

print(persona4)
print(persona5)
print(persona6)

#-------------------------------------------------------------------------------

persona4.calcularIMC()
persona4.esMayorDeEdad()

persona5.calcularIMC()
persona5.esMayorDeEdad()

persona6.calcularIMC()
persona6.esMayorDeEdad()

#print(persona4)