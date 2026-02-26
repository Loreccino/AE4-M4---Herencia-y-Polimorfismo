"""
AE-4 - HERENCIA Y POLIMORFISMO
SISTEMA FORMAS GEOMÉTRICAS
"""
import math


#  crear clase Figura + metodo calcular_area()
class Figura:
    def calcular_area(self):
        pass  # pass será sobreescrito por las subclases


#  subclases figuras + heredar de Figura + sobreescribir metodo
class Rectángulo(Figura):
    def __init__(self):
        super().__init__()
        pass

class Cuadrado(Figura):
    def __init__(self):
        super().__init__()
        pass


class Triangulo(Figura):
    def __init__(self):
        super().__init__()
        pass



#  demostrar polimorfismo con lista de figuras + calcular área de cada una

figuras = [ 
    Rectángulo(5, 7)
    Cuadrado(4),
    Triangulo(7)
    ]

