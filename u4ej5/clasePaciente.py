import json

class Paciente:
    __nombre: str
    __apellido: str
    __altura: int
    __peso: float
    __telefono: str


    def __init__(self, nombre, apellido, telefono, altura, peso):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__altura = int(altura) #en cm
        self.__peso = float(peso)   #en kg

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura
    
    def getPeso(self):
        return self.__peso
    
    def getIMC(self):
        imc = self.__peso/((self.__altura/100)**2)
        return imc

    def modificar(self, nombre, apellido, telefono, altura, peso):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__altura = int(altura)
        self.__peso = float(peso)
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
                telefono = self.__telefono,
                altura = self.__altura,
                peso = self.__peso
            )
        )
        return d