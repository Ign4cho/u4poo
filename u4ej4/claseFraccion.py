from ast import Num
import math
from re import T

class Fraccion:
    __numerador: int
    __denominador: int

    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError
        else:
            self.__numerador = num
            self.__denominador = den

    def __str__(self):
        return f'{self.__numerador}/{self.__denominador}'

    def __add__(self, other):

        if self.__denominador == other.getDen():
            num = self.__numerador + other.getNum()
            den = self.__denominador
        else: 
            den = self.__denominador * other.getDen()
            num = self.__numerador*other.getDen() + self.__denominador*other.getNum()
        return Fraccion(num, den)

    def __sub__(self, other):
        other.setNum(-(other.getNum()))
        return self + other
    
    def __mul__(self, other):
        num = self.__numerador * other.getNum()
        den = self.__denominador * other.getDen()
        return Fraccion(num, den)
    
    def __truediv__(self, other):
        num = self.__numerador * other.getDen()
        den = self.__denominador * other.getNum()
        return Fraccion(num, den)
    
    def simplificar(self):
        if abs(self.__numerador) < abs(self.__denominador):
            dmc = abs(self.__numerador)
        else:
            dmc = abs(self.__denominador)
        
        while dmc > 1:
            if (self.__numerador % dmc)==0 and (self.__denominador % dmc)==0:
                self.setNum(int(self.__numerador/dmc))
                self.setDen(int(self.__denominador/dmc))

            dmc-=1
        

    def getNum(self):
        return self.__numerador

    def getDen(self):
        return self.__denominador

    def setNum(self, nuevo):
        self.__numerador = nuevo
    
    def setDen(self, nuevo):
        self.__denominador = nuevo