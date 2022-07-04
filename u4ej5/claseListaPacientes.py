from clasePaciente import Paciente
from tkinter import messagebox
import tkinter as tk


class ListaPacientes(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, paciente, index=tk.END):
        text = f'{paciente.getNombre()}, {paciente.getApellido()}'
        self.lb.insert(index, text)
    
    def borrar(self, index):
        self.lb.delete(index)

    def modificar(self, paciente, index):
        self.borrar(index)
        self.insertar(paciente, index)

    def bind_doble_clik(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind('<Double-Button-1>', handler)