from clasePaciente import Paciente
from claseObjectEncoder import ObjectEncoder
from manejadorPacientes import Manejador

class RepositorioPacientes:
    __conn = None
    __manejador = None

    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()
    
    def agregarPaciente(self, paciente):
        self.__manejador.agregarElemento(paciente)

    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente

    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
