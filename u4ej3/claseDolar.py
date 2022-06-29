import json
from tkinter.messagebox import NO
from urllib.request import urlopen

class Dolar:
    __resultado = None

    def __init__(self) -> None:
        self.__resultado = None

    def run(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        print(url_template)
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    
    def getDatos(self):
        return self.__resultado
        
