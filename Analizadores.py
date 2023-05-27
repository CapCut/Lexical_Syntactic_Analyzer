from Clases import *
from tkinter import messagebox

class Scanner:
    def __init__(self):
        #Declaramos una lista para los tokens y errores léxicos
        self.listaTokens = []
        self.listaErroes = []
        #Declaramos en una lista las palabras reservadas de nuestro lenguaje
        self.reservadas = []
        #Declaramos un a lista para el analizador sintáctico y una para sus errores
        self.sintactic = []
        self.error_sin = []

    def Analizador(self, char):
        #LLamamos a nuestras listas declaradas en el constructor de la clase Scanner
        self.listaErroes = []
        self.listaTokens = []

        #Utilizaremos un try except para que el programa nos muestre con mejor facilidad los errores (Es opcional colocar el try except)
        try:#Verificamos si en las listas no hay caracteres, si no hay caracteres se procede con toda la instrucción del if, de lo contrario pasara al else.
            if (self.listaTokens and self.listaErroes) != None:
                char += '&'#Esta variable nos servira para deterctar el final de nuestro contenido a analizar
                linea = 1#Se inicializa en 1 para hacer coincidir nuestra posición "x" en el editor de texto
                columna = 1#Se inicializa en 0 para hacer coincidir nuestra posición "y" en el edito.
                iterador = 0#Esta variable sevira para ir contando cuantos carácteres se leeran en el archivo que cargaremos
                mufa = ''#Esta variable irá almacenando todas las variables que la variable "iterador" vaya detectando o contando
                estado = 'S0'#Esta variable corresponde a nuestro estado de aceptación de nuestro AFD 

                #Utilizaremos un bucle while para 
                while iterador < len(char):
                    caracter = char[iterador]#Esta variable auxiliar servira para compara los caracteres que se declararo en el archivo
                                             #"Descripción.txt", y en las sentencias if, guardaremos esos caracteres en nuestra lista de tokens o en la lista de errores
                    if estado == 'S0':#Los estados serán segun nuestro AFD en la carpeta de "Resours/AFD"
                        if caracter == '<':#Comparamos el caracter con lo que necesitamos analizar
                            mufa = caracter#Almacenamos el caracter
                            columna += 1#Avanzamos una posición para depsues guardarla en la lista de tokens
                            self.listaTokens.append(Token(mufa, 'TK_MENOR_QUE', linea, columna))#Se guarda el caracter en la lista de tokens
                            mufa = ''#Vaciamos la variabre que almacena los tokens o los caracteres
                            estado = 'S0'#Regresamos a nuestro estado inicial o de aceptación en este caso
                        elif caracter == '!':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_EXCLAMAR_A', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == '-':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_GION', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == ';':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_PUNTO_COMA', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == ':':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_2_PUNTOS', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == '>':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_MAYOR_QUE', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == '.':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_PUNTO', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == '(':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_PARENTESIS_A', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == ')':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_PARENTESIS_C', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == ',':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_COMA', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == '"':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'TK_COMILLAS_DOBLE', linea, columna))
                            mufa = ''
                            estado = 'S0'
                        elif caracter == '\n':
                            columna = 1
                            linea += 1
                        elif caracter == ' ':
                            columna += 1
                        elif caracter == '\t':
                            columna += 1
                        elif caracter.isalpha():
                            mufa = caracter
                            columna += 1
                            estado = 'S1'
                        elif caracter.isdigit():
                            mufa = caracter
                            columna += 1
                            estado = 'S2'
                        elif caracter == '/' and (char[iterador + 1] == '*'):
                            mufa = caracter
                            columna += 1
                            estado = 'S3'
                        elif caracter == '/':
                            mufa = caracter
                            columna += 1
                            estado = 'S4'
                        elif caracter == '&':
                            mufa = caracter
                            columna += 1
                            self.listaTokens.append(Token(mufa, 'FIN_ANALISIS', linea, columna))
                            mufa = ''
                            estado = 'S0'
                            messagebox.showinfo('Análisis', 'Analisis exitoso []~(￣▽￣)~*')
                            print('\n')
                        else:
                            self.listaErroes.append(Error(caracter, 'ERROR', 'Léxico', linea, columna))
                            mufa = ''
                            columna = 0

                    elif estado == 'S1':#En este estado verificaremos si el caracter es letra o numero, cualquiera de los casos se lamacenaran en la variable "mufa"
                        if caracter.isalpha() or (caracter.isdigit()):
                            mufa += caracter
                            columna += 1
                            estado = 'S1'
                        else:#Aquí validaremos si la variable caracter es igual a nuestras palabras reservadas dentro de nuestro lenguaje
                            if mufa == 'Etiqueta':
                                self.listaTokens.append(Token(mufa, 'TK_ETIQUETA_R', linea, columna))
                                mufa = ''
                                iterador -= 1#Esta acción es para salir de la sentencia y seguir verificando si es o no una palabra resevada
                                estado = 'S0'
                            elif mufa == 'Boton':
                                self.listaTokens.append(Token(mufa, 'TK_BOTON_R', linea, columna))
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'
                            elif mufa == 'Check':
                                self.listaTokens.append(Token(mufa, 'TK_CHECK_R', linea, columna))
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'
                            elif mufa == 'RadioBoton':
                                self.listaTokens.append(Token(mufa, 'TK_RADIOBOTON_R', linea, columna))
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'
                            elif mufa == 'Texto':
                                self.listaTokens.append(Token(mufa, 'TK_TEXTO_R', linea, columna))
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'
                            elif mufa == 'AreaTexto':
                                self.listaTokens.append(Token(mufa, 'TK_AREATEXTO_R', linea, columna))
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'
                            elif mufa == 'Clave':
                                self.listaTokens.append(Token(mufa, 'TK_CLAVE_R', linea, columna))
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'
                            elif mufa == 'Contenedor':
                                self.listaTokens.append(Token(mufa, 'TK_CONTENEDOR_R', linea, columna))
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'
                            else:#Si la variable "mufa" no es una palabra recervada llegamos a este else para guardar los caracteres de la varialbe "mufa"
                                self.listaTokens.append(Token(mufa, 'TK_CADENA', linea, columna))#Como una cadena que continee letras, números u otros caracteres que no son parte de nuestro lenguaje
                                mufa = ''
                                iterador -= 1
                                estado = 'S0'

                    elif estado == 'S2':
                        if caracter.isdigit():
                            mufa += caracter
                            columna += 1
                            estado = 'S2'
                        else:
                            self.listaTokens.append(Token(mufa, 'TK_NUMERO', linea, columna))
                            mufa = ''
                            estado = 'S0'

                    elif estado == 'S3':
                        if caracter == '*':
                            mufa += caracter
                            columna += 1
                            if char[iterador + 1] == '/':
                                mufa += char[iterador + 1]
                                columna += 1
                                self.listaTokens.append(Token(mufa, 'TK_COMENT_MULTI', linea, columna))
                                mufa = ''
                                iterador += 1
                                estado = 'S0'
                        elif caracter == '\n':
                            mufa += caracter
                            columna += 1
                            linea += 1
                        else:
                            mufa += caracter
                            columna += 1
                            estado = 'S3'

                    elif estado == 'S4':
                        if caracter == '/':
                            mufa += caracter
                            columna += 1
                            estado = 'S5'

                    elif estado == 'S5':
                        if caracter == '\n':
                            mufa += caracter
                            self.listaTokens.append(Token(mufa, 'TK_COMENT_SIMPLE', linea, columna))
                            mufa = ''
                            columna = 0
                            linea += 1
                            estado = 'S0'
                        else:
                            mufa += caracter
                            columna += 1
                            estado = 'S5'

                    iterador += 1
            else:
                print('No se puede analizar el archivo')
        except Exception as e:
            print(e)
    
    def imprimir_analizador(self):
        print("__________ T O K E N S __________")
        for i in self.listaTokens:
            i.getInfoTokens()
        print()

        print("__________ E R R O R E S __________")
        for j in self.listaErroes:
            j.getInfoErrores()
        print()
    
    def obtener_lista_tokens(self):
        return self.listaTokens

    def obtener_lista_error(self):
        return self.listaErroes

    def obtener_lista_err_sintactico(self):
        return self.error_sin