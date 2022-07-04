from gc import callbacks
from claseFormPacientes import FormPacientes
import tkinter as tk


class ActualizaPaciente(FormPacientes):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text = 'Guardar')
        self.btn_delete = tk.Button(self, text = 'Borrar')
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)