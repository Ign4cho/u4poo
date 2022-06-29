from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Aplicacion():
    __ventana = None
    __altura: None
    __peso: None
    __imc: None
    __cc: None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('300x180')
        self.__ventana.title('Calculadora de IMC')
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__imc = StringVar()
        self.__cc= StringVar(value='Composición corporal ')
        self.alturaEntry = ttk.Entry(mainframe, width = 7, textvariable=self.__altura)
        self.alturaEntry.grid(column=2, row=1, sticky=(W, E))
        self.pesoEntry = ttk.Entry(mainframe, width=7, textvariable=self.__peso)
        self.pesoEntry.grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text='Calcular', command=self.calcular).grid(column=1, row=3)
        ttk.Button(mainframe, text='Limpiar', command=self.limpiar).grid(column=2, row=3, sticky=W)
        ttk.Label(mainframe, text='Altura:').grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text='Cm').grid(column=3, row=1,sticky=E)
        ttk.Label(mainframe, text='Peso:').grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text='Kg').grid(column=3, row=2,sticky=E)
        ttk.Label(mainframe, text='Tu imc es').grid(column=1, row=4)
        ttk.Label(mainframe, textvariable=self.__imc).grid(column=2, row=4, sticky=E)
        ttk.Label(mainframe, text='kg/m2').grid(column=3, row=4, sticky=E)
        ttk.Label(mainframe, textvariable=self.__cc).grid(column=2, row=5, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.alturaEntry.focus()
        self.__ventana.mainloop()
    
    def calcular(self):
        try:
            peso = float(self.pesoEntry.get())
            altura = float(self.alturaEntry.get())
            valor = peso/((altura/100)**2)
            self.__imc.set(f'{valor:.1f}')
            self.actualizaComposicion(valor)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
            self.__altura.set('')
            self.__peso.set('')
            self.__imc.set('')
            self.__cc.set('Composición corporal')
            self.alturaEntry.focus()
    
    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.__imc.set('')
        self.__cc.set('Composición corporal')
        self.alturaEntry.focus()

    def actualizaComposicion(self, valor):
        if float(valor ) < 18.5:
            self.__cc.set('Peso inferior al normal')
        elif float(valor) < 24.9:
            self.__cc.set('Peso normal')
        elif float(valor) < 29.9:
            self.__cc.set('Peso superior al normal')
        else:
            self.__cc.set('Obesidad')