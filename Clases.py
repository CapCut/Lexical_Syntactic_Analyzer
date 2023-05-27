class Token:
    def __init__(self, lexema, tipo, line, colum):
        self.lexema = lexema
        self.tipo = tipo
        self.line = line 
        self.colum = colum
    
    def getInfoTokens(self):
        print('_'*40)
        print('Lexema: ', self.lexema, ' |Tipo: ', self.tipo, ' |Linea: ', self.line, ' |Columna: ', self.colum)

    def getToken(self):
        print("|{:<4} | {:<7} |".format(self.lexema, self.tipo))
    
class Error:
    def __init__(self, caracter, descripcion, tipo, line, colum):
        self.caracter = caracter
        self.descripcion = descripcion
        self.tipo = tipo
        self.line = line
        self.colum = colum

    def getInfoErrores(self):
        print('_'*40)
        print(self.caracter, '|Descripción: ', self.descripcion, ' |Tipo: ', self.tipo, ' |Linea: ', self.line, ' |Columna: ', self.colum)