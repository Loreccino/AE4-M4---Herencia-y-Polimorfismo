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
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def calcular_area(self):
        return self.l1 * self.l2   # lado 1 * lado 2
    

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado ** 2

class Triángulo(Figura):
    def __init__(self, base, alt):
        self.base = base
        self.alt = alt
    def calcular_area(self):
        return (self.base * self.alt) / 2


#  demostrar polimorfismo con lista de figuras + calcular área de cada una

figuras = [ 
        Rectángulo(5, 7),
        Cuadrado(4),
        Triángulo(7, 12)
    ]

print("ÁREA DE FIGURAS: \n")
for i, figura in enumerate(figuras, 1):
    area = figura.calcular_area()
    print(f"{i} - {figura.__class__.__name__} - {area:2f}")