from Clases.Punto import *
from Clases.Rectangulo import *

if __name__ == "__main__":

    #Primer punto
    print("Punto A")
    a = Punto(2,3)
    print(a.string())

    print("Punto B")
    b = Punto(5,5)
    print(b.string())

    print("Punto C")
    c = Punto(-3,-1)
    print(c.string())

    print("Punto D")
    d = Punto(0,0)
    print(d.string())

    #Segundo punto
    a.cuadrante()
    c.cuadrante()
    d.cuadrante()

    #Tercer punto
    print("Vector AB")
    print(a.vector(b))

    print("Vector BA")
    print(b.vector(a))

    #Cuarto punto
    print("Distancia AB")
    a.distancia(b)

    #Quinto punto
    a.disntacia((0,0))
    b.disntacia((0,0))
    c.disntacia((0,0))

    if a.disntacia((0,0)) < b.disntacia((0,0)) and a.disntacia((0,0)) < c.disntacia((0,0)):
        print("El punto A es el que más cerca está del origen")
    elif b.disntacia((0,0)) < a.disntacia((0,0)) and b.disntacia((0,0)) < c.disntacia((0,0)):
        print("El punto B es el que más cerca está del origen")
    else:
        print("El punto C es el que más cerca está del origen")
    
    #Sexto punto
    rectangulo = Rectangulo(a, b)

    #Séptimo punto
    