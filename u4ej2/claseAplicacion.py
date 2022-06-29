from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk

from pip import main

class Aplicacion():
    __ventana = None
    __preciobase = None
    __precioIva = None
    __diferencia = None
    __tipoIva = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculadora IVA')
        self.__ventana.geometry('150x150')
        self.__ventana.config(padx=5, pady=5)
        self.__preciobase = StringVar()
        self.__precioIva = StringVar()
        self.__diferencia = StringVar()
        self.__tipoIva = IntVar()
        
        mainframe = tk.Frame(self.__ventana)
        mainframe.grid(row=0,column=0, sticky=W)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text='Precio sin IVA').grid(row=0, column=0, sticky=W)
        self.precioEntry = ttk.Entry(mainframe, width=6, textvariable=self.__preciobase)
        self.precioEntry.grid(row=0, column=1, sticky=E)

        labelFrameRadio = ttk.Labelframe(mainframe, text='Seleccione:')
        labelFrameRadio.grid(column=0, row=1, sticky = W)
        ttk.Radiobutton(labelFrameRadio, text='IVA 21%', value=0, variable=self.__tipoIva, command=self.calculaIVA).grid(column=0, row=0, sticky=W)
        ttk.Radiobutton(labelFrameRadio, text='IVA 10,5%', value=1, variable=self.__tipoIva, command=self.calculaIVA).grid(column=0, row=1, sticky=W)

        ttk.Label(mainframe, text='Precio con IVA').grid(row=2, column=0, sticky=S)
        ttk.Label(mainframe, textvariable=self.__precioIva).grid(row=2, column=1, sticky=S)
        ttk.Label(mainframe, text='IVA').grid(row=3, column=0)
        ttk.Label(mainframe, textvariable=self.__diferencia).grid(row=3, column=1)     
        self.__tipoIva.set(-1)
        self.__ventana.mainloop()

    def calculaIVA(self):
        try:
            base = float(self.__preciobase.get())
            if self.__tipoIva.get() == 1:
                dif = base*(10.5/100)
            elif self.__tipoIva.get() == 0:
                dif = base*(21/100)
            self.__precioIva.set(base+dif)
            self.__diferencia.set(dif)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
            self.__preciobase.set('')
            self.__diferencia.set('')
            self.__tipoIva.set(-1)
            self.__precioIva.set('')
            self.precioEntry.focus()

