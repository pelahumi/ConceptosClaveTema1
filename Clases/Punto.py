from cmath import sqrt
import math

class Punto():

    #Constuctor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Getters
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    #Setters
    def set_x(self, x, y):
        if x == "":
            self.x = 0
        if y == "":
            self.y = 0
        else:
            self.x = x
            self.y = y

    #Método string
    def string(self):
        pto = (self.x, self.y)
        return pto

    #Método cuadrante
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Estás en el primer cuadrante.")
        
        elif self.x < 0 and self.y > 0:
            print("Estás en el segundo cuadrante")

        elif self.x < 0 and self.y < 0:
            print("Estás en el tercer cuadrante")

        elif self.x >0 and self.y < 0:
            print("Estás en el cuarto cuadrante")
        
        elif self.x == 0 and self.y != 0:
            print("Estás en el eje horizontal")
        
        elif self.x != 0 and self.y == 0:
            print("Estás en el eje vertical")
        
        else:
            print("Estás en el origen de coordenadas")

    #Método vector
    def vector(self, pto):
        a = (self.x - pto[0])
        b = (self.y - pto[1])
        pto2 = (a, b)
        return pto2

    #Método distancia
    def distancia(self, pto):
        vector = self.vector(pto)

        a = vector[0]**2
        b = vector[1]**2

        distancia = sqrt(a + b)

        return distancia

punto = Punto(5,8)
print(punto.distancia((3,1)))

    
        
    
