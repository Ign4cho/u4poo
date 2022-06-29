from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from claseDolar import Dolar


from pip import main

class Aplicacion(tk.Tk):
    __pesos = None
    __dolar = None
    __cambio = float

    def __init__(self):
        super().__init__()
        self.geometry('300x150')
        self.title('Conversor dolar-pesos')
        self.config(padx=5, pady=5)

        self.__pesos = StringVar()        
        self.__dolar = StringVar()
        self.__cambio = self.getCambio()

        mainframe = ttk.Frame(self)
        mainframe.grid(row=0, column=0, sticky=W)  
        mainframe.rowconfigure(0, weight=1)

        self.dolarEntry = ttk.Entry(mainframe, width=7, textvariable=self.__dolar)
        self.dolarEntry.grid(row=0, column=1, sticky=W)
        ttk.Label(mainframe, text='dolares').grid(row=0, column=2, sticky=W)

        ttk.Label(mainframe, text='Es equivalente a').grid(row=1, column=0, sticky=W)
        ttk.Label(mainframe, textvariable=self.__pesos).grid(row=1, column=1, sticky=W)
        ttk.Label(mainframe, text='pesos').grid(row=1, column=2, sticky=W)

        ttk.Button(mainframe, text='Salir', command=self.destroy).grid(row=2, column=1, sticky=W)
        ttk.Button(mainframe, text='Calcular', command=self.calculaCambio).grid(row=2, column=0, sticky=W)
        self.mainloop()



    def calculaCambio(self):
        try:
            self.__dolar.set(self.__dolar.get().replace(',', '.'))
            self.__pesos.set(float(self.__dolar.get())*self.__cambio)

        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Ingrese un número')
            self.__pesos.set('')
            self.__dolar.set('')

    def getCambio(self):
        d = Dolar()
        d.run()
     
        datos = d.getDatos()
        venta = datos[0]['casa']['venta']
        venta = venta.replace(',', '.')
        
        return float(venta)