class Electrodomestico:
    def __init__(self, precio_base=100, color="Blanco", consumo_elctrico="F", peso=500):
        self.__precio_base = precio_base
        self.__color = color
        self.__consumo_elctrico = consumo_elctrico
        self.__peso = peso

    def esEredable(self):
        return print("El producto es eredable")

    def __str__(self):
        return f"Electrodomestico: precio_base= ${self.__precio_base}, color= {self.__color}, consumo elctrico= {self.__consumo_elctrico}, peso= {self.__peso}g"
    
#----------------------------------------------------

producto1 = Electrodomestico()
producto2 = Electrodomestico(precio_base=300, peso=1000)
producto3 = Electrodomestico(150, "plateado", "A", 600)    

print(producto1)
print(producto2)
print(producto3)

producto1.esEredable()