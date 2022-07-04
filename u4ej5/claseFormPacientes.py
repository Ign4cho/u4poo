from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from clasePaciente import Paciente

class FormPacientes(tk.LabelFrame):
    fields = ('Nombre', 'Apellido', 'Telefono', 'Altura', 'Peso')

    def __init__(self, master, **kwargs):
        super().__init__(master, text='Contacto', padx=5, pady=5, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=20)
        label.grid(row=position, column=0)
        entry.grid(row=position, column=1)
        return entry
    
    def mostrarPacienteFormulario(self, paciente):            
        values = (paciente.getNombre(), paciente.getApellido(), paciente.getTelefono(), paciente.getAltura(),paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def crearPaciente(self):
        values=[e.get() for e in self.entries]
        paciente=None
        try:
            paciente = Paciente(*values)
        except ValueError as e:
            messagebox.showerror('Error de validación', str(e), parent=self)
        return paciente

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
