import math

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
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
    
        

    
