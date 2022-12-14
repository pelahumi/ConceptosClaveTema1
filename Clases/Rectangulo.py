import math

class Rectangulo():

    #Constructor
    def __init__(self, pto1, pto2):
        self.pto1 = pto1
        self.pto2 = pto2

    #Getters
    def get_pto1(self):
        return self.pto1

    def get_pto2(self):
        return self.pto2

    #Setters
    def set_pto1(self, pto1):
        if pto1 == "":
            pto1 = (0,0)
        else:
            self.pto1 = pto1

    def set_pto1(self, pto2):
        if pto2 == "":
            pto2 = (0,0)
        else:
            self.pto2 = pto2
    
    #Método base
    def base(self):
        b1 = self.pto1
        b2 = (self.pto2[0], self.pto1[1])
        base = b1, b2

        return b1, b2
    
    #Método altura
    def altura(self):
        a1 = self.pto1
        a2 = (self.pto1[0], self.pto2[1])
        altura = a1, a2

        return a1, a2

    ####
    def distancia(self, pto1):
        vector = (self.pto1[0] - self.pto2[0], self.pto1[1] - self.pto2[1])

        a = vector[0]**2
        b = vector[1]**2

        distancia = math.sqrt(a + b)

        return distancia
    ###

    #Método área
    def area(self):
        base = self.base()
        distancia_base = self.distancia(base)
        altura = self.altura()
        distancia_altura = self.distancia(altura)

        area = distancia_base * distancia_altura
        return area


    