import json
from pathlib import Path
from clasePaciente import Paciente
from manejadorPacientes import Manejador

class ObjectEncoder(object):
    __pathArchivo = None
    def __init__(self, pathArchivo):
        self.__pathArchivo = pathArchivo
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                pacientes=d['pacientes']
                dPacientes = pacientes[0]
                lista=class_()
                for i in range(len(pacientes)):
                    dPacientes=pacientes[i]
                    class_name=dPacientes.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPacientes['__atributos__']
                    unPaciente=class_(**atributos)
                    lista.agregarElemento(unPaciente)
            return lista
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)