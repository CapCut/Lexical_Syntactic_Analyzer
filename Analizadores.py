from Clases import *
from tkinter import messagebox

class Scanner:
    def __init__(self):
        self.listaTokens = []
        self.listaErroes = []
        self.reservadas = []
        self.sintactic = []
        self.error_sin = []
        self.contador = 0

    def Analizador(self, char):
        self.listaErroes = []
        self.listaTokens = []