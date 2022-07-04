from clasePaciente import Paciente
import json

class Manejador:
    __pacientes = []
    indice = 0
    def __init__(self):
        self.__pacientes = []
        self.indice=0

    def agregarElemento(self, unPaciente):
        unPaciente.rowid = Manejador.indice
        Manejador.indice += 1
        self.__pacientes.append(unPaciente)

    def deletePaciente(self, paciente):
        index = self.obtenerIndice(paciente)
        self.__pacientes.pop(index)

    def updatePaciente(self, paciente):
        index = self.obtenerIndice(paciente)
        self.__pacientes[index] = paciente

    def obtenerIndice(self, paciente):
        band = False
        i=0
        while not band and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == paciente.rowid:
                band = True
            else:
                i+=1
                
        return i

    def getListaPacientes(self):
        return self.__pacientes

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__pacientes]
        )
        return d