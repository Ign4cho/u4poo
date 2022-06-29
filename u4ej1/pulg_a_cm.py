# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:06:47 2020

@author: morte
"""
from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana=None
    __pulgadas=None
    __centimetros=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor Pulgadas a Centímetros')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__pulgadas = StringVar()
        self.__centimetros = StringVar()
        self.pulgadasEntry = ttk.Entry(mainframe, width=7, textvariable=self.__pulgadas)
        self.pulgadasEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__centimetros).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="pulgadas").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="centímetros").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.pulgadasEntry.focus()
        self.__ventana.mainloop()
    def calcular(self):
        try:
            valor=float(self.pulgadasEntry.get())
            self.__centimetros.set(2.54*valor)
        except ValueError:
            messagebox.showerror(title='Error de tipo',
                                 message='Debe ingresar un valor numérico')
            self.__pulgadas.set('')
            self.pulgadasEntry.focus()

def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()