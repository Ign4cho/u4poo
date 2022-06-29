# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 23:03:53 2020

@author: morte
"""
from claseFraccion import Fraccion
from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primeraFraccion=None
    __segundaFraccion=None
    __dividendo=None
    __divisor=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None

        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=self.ponerBARRA).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe, text='Limpiar', command=self.borrarPanel).grid(column=2, row=8, sticky=W)

        self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()
    
    def ponerNUMERO(self, num):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            self.__panel.set(valor+num)
        else: 
            self.__operadorAux = None
            self.__panel.set(num)
    
    def borrarPanel(self):
        self.__panel.set('')
        self.__operador.set('')
        self.__primeraFraccion = None
        self.__segundaFraccion= None

    def resolverOperacion(self, fraccion1, fraccion2, operacion):
        resul = 0
        if operacion == '+':
            resul = fraccion1+fraccion2
        elif operacion == '-':
            resul = fraccion1 - fraccion2
        elif operacion == '*':
            resul = fraccion1*fraccion2
        elif operacion == '%':
            resul = fraccion1/fraccion2
        resul.simplificar()
        self.__panel.set(str(resul))
        self.__primeraFraccion = resul

    def ponerOPERADOR(self, op):
        if op == '=':
            if isinstance(self.__primeraFraccion, Fraccion):
                operacion = self.__operadorAux
                self.__divisor = int(self.__panel.get())
                self.__segundaFraccion = Fraccion(self.__dividendo, self.__divisor)
                print(operacion)
                self.resolverOperacion(self.__primeraFraccion, self.__segundaFraccion, operacion)
                
            else:
                messagebox.showerror(title='Faltan fracciones', message='No ha ingresado dos fracciones')
                self.borrarPanel()
        else:
            
            divisor = self.__panel.get()       
            self.__divisor = int(divisor)
            self.__primeraFraccion = Fraccion(self.__dividendo, self.__divisor)
            self.__panel.set('')
            self.__operador.set(op)
            self.__operadorAux = op

    def ponerNUMERO(self, num):
        valor = self.__panel.get()
        self.__panel.set(valor+num)


    def ponerBARRA(self):
        self.__operador.set('/')
        self.__dividendo = int(self.__panel.get())
        self.__panel.set('')

