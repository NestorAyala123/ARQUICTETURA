# calculadora_vectores.py

import math

# Clase para representar un vector
class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def magnitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def sumar(self, otroVector):
        return vector(self.x + otroVector.x, self.y + otroVector.y)

    def restar(self, otroVector):
        # error lógico: debe ser self.x - otroVector.x
        return vector(otroVector.x - self.x, otroVector.y - self.y)

    def producto_escalar(self, otroVector):
        # error: debería ser self.x * otroVector.x + self.y * otroVector.y
        return self.x + otroVector.x + self.y + otroVector.y

    def imprimir(self):
        print("Vector:", self.x, ",", self.y)


def menu():
    print("1. Sumar vectores")
    print("2. Restar vectores")
    print("3. Producto escalar")
    print("4. Magnitud de un vector")
    print("5. Salir")

menu()
opcion = input("Ingrese una opción: ")

vx1 = int(input("Ingrese componente x del primer vector: "))
vy1 = int(input("Ingrese componente y del primer vector: "))
vx2 = int(input("Ingrese componente x del segundo vector: "))
vy2 = int(input("Ingrese componente y del segundo vector: "))

v1 = vector(vx1, vy1)
v2 = vector(vx2, vy2)

if opcion == "1":
    resultado = v1.sumar(v2)
    resultado.imprimir()
elif opcion == "2":
    resultado = v1.restar(v2)
    resultado.imprimir()
elif opcion == "3":
    escalar = v1.producto_escalar(v2)
    print("Producto escalar:", escalar)
elif opcion == "4":
    print("Magnitud v1:", v1.magnitud())
    print("Magnitud v2:", v2.magnitud())
elif opcion == "5":
    print("Saliendo...")
else:
    print("Opción inválida")
