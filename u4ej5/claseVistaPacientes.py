import tkinter as tk
from typing import List
from claseListaPacientes import ListaPacientes
from claseFormPacientes import FormPacientes
from claseActualizaPaciente import ActualizaPaciente

class VistaPacientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lista de pacientes')
        self.list = ListaPacientes(self, height=15)
        self.form = ActualizaPaciente(self)
        self.btn_new = tk.Button(self, text='Agregar Paciente')
        self.list.pack(side=tk.LEFT, padx = 10, pady=10)
        self.form.pack(padx=10,pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_clik(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)

    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)
    
    def modificaPaciente(self, paciente, index):
        self.list.modificar(paciente, index)

    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    
    def obtenerDetalles(self):
        return self.form.crearPaciente()

    def verPacienteEnForm(self, paciente):
        self.form.mostrarPacienteFormulario(paciente)