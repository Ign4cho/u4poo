from claseRepositorioPacientes import RepositorioPacientes
from claseVistaPacientes import VistaPacientes
from manejadorPacientes import Manejador
from claseObjectEncoder import ObjectEncoder
from claseControlador import Controlador

def main():
    conn = ObjectEncoder('datosPacientes.json')
    repo = RepositorioPacientes(conn)
    vista = VistaPacientes()
    ctrl = Controlador(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()


if __name__ == '__main__':
    main()