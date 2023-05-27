#====================LIBRERIAS====================
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog, scrolledtext
import tkinter as tk
from tkinter import BOTTOM, Menu, Scrollbar, Tk, XView, font, ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle
from Analizadores import *

#====================VARIABLES====================
ventana = None
scroll = None

ventana_token = None
ventana_error = None

cadena = ""
ruta = ""
bandera = False

correlativo = None
token = None
lexema = None
tipo = None
descipcion = None
line = None
colum = None

scannergg = Scanner()
#=================INTERFAZ GRÁFICA=================
#Nuevo
def nuevo():
    global scroll

    respuesta = messagebox.askyesno('Guardar', '¿Deseas guardar el contenido del área de texto?')

    if respuesta:
        texto_guardar = scroll.get('1.0', 'end-1c')
        pendragon = filedialog.asksaveasfilename(title="Guardar Archvio", filetypes=(("all files", "*.*"),("LFP files", "*.css"), ("Text Files", "*.txt"),("HTML5 Files", "*.html")))
    
        with open(pendragon, 'w', encoding='utf-8') as archivo:
            archivo.write(texto_guardar)
            archivo.close()
        messagebox.showinfo('Guardado', 'Archivo guardado correctamente.')
    else:
        scroll.delete('1.0', 'end')
        messagebox.showerror('Aviso', 'Archivo eliminado.')
    
#Abrir
def abrir():
    global cadena
    global scroll
    global bandera
    global ruta

    ruta = filedialog.askopenfilename(title="Abrir Archivo", filetypes=(("all files", "*.*"),("LFP files", "*.css"), ("Text Files", "*.txt"),("HTML5 Files", "*.html")))

    try:
        if (ruta != ""):
            if (bandera == False):
                cadena = open(ruta, 'r', encoding='utf-8')
                contenido = cadena.read()
                scroll.insert(tk.INSERT, contenido)
                print("\n", contenido, "\n")
                cadena.close()
                bandera = True
                messagebox.showinfo('Aviso', 'Archivo Cargado con Éxito.')
            else:
                messagebox.showwarning('Alerta', 'Ya se encuentra un archivo.')
        else:
            messagebox.showerror('ERROR', 'No se cargó ningun archivo.')
    except:
        pass

#Guardar
def guardar():
    global ruta
    global scroll

    guardar = scroll.get(1.0, tkinter.END)

    try:
        archivo = open(ruta, 'w', encoding='utf-8')
        archivo.write(guardar)
        archivo.close()
        messagebox.showinfo('Aviso', 'Se a editado el archivo correctamente.')
    except:
        pass

#Guardar Como
def guardar_como():
    global scroll

    guardar_Como = scroll.get(1.0, tkinter.END)
    arturia = filedialog.asksaveasfilename(title="Guardar Archvio", filetypes=(("all files", "*.*"),("LFP files", "*.css"), ("Text Files", "*.txt"),("HTML5 Files", "*.html")))

    try:
        archivox = open(arturia, 'w', encoding='utf-8')
        archivox.write(guardar_Como)
        archivox.close()
        messagebox.showinfo('Aviso', 'Archivo guardado correctamente.')
    except:
        pass

#Salir

#Análisis
def analisis():
    global ruta
    global cadena
    global scroll
    global scannergg

    #conten = scroll.get(1.0, tkinter.END)
    
    #if conten != "":
    #    scannergg.Analizador(conten)
    #    scannergg.imprimir_analizador()
    #    scannergg.sintactico()
    #    scannergg.imprimir_parser()
    #
    #    aux_lex = scannergg.listaErroes
    #    aux_sin = scannergg.error_sin
#
    #    if (aux_sin and aux_lex) != None:
    #        scannergg.escribir_sentencias(ruta)
    #    else:
    #        pass
    #else:
    #    messagebox.showerror('Error', 'No se pudo analizar el archivo')
        
#Ver Tokens
def ventana_mostrar_token():
    global ventana_token
    global scannergg

    ventana_token = tk.Tk()
    ventana_token.resizable(0, 0)
    ventana_token.config(width="750", height="300", bg="#38045E", relief="raised", bd="10", cursor="hand2")
    ventana_token.title("Ver Tokens")

    #Se crea una instancia de ThemedStyle
    estilo = ThemedStyle(ventana_token)
    # Establecer un tema
    estilo.set_theme("clam")
    # Configurar el estilo del Treeview utilizando CSS
    estilo.configure("Custom.Treeview", background="red", foreground="black", font=('Arial', 12))

    #Tabla de datos
    tabla = ttk.Treeview(ventana_token, columns=("Elemento1", "Elemento2"), style="Custom.Treeview")
    tabla.column("#0", width=100)
    tabla.column("Elemento1", width=350, anchor=CENTER)
    tabla.column("Elemento2", width=200, anchor=CENTER)
    
    tabla.heading("#0", text='Correlativo', anchor=CENTER)
    tabla.heading("Elemento1", text='Lexema', anchor=CENTER)
    tabla.heading("Elemento2", text='Token', anchor=CENTER)

    #Función Lógica
    #aux_tabla = scannergg.obtener_lista_tokens()
    #nuevos = []
#
    #for j in aux_tabla:
    #    nuevos.append((j.lexema, j.tipo))
#
    #iterador = 1
    #for i in nuevos:
    #    tabla.insert("", tk.END, text=str(iterador), values=i)
    #    iterador += 1

    tabla.pack()
    tabla.place(x=30, y=30)

    ventana_token.mainloop()


#Errores
def ventana_mostrar_error():
    global ventana_error
    global scannergg

    ventana_error = tk.Tk()
    ventana_error.resizable(0, 0)
    ventana_error.config(width="800", height="300", bg="#38045E", relief="raised", bd="10", cursor="hand2")
    ventana_error.title("Ver Errores") 

    #Se crea una instancia de ThemedStyle
    estilo = ThemedStyle(ventana_error)
    # Establecer un tema
    estilo.set_theme("clam")
    # Configurar el estilo del Treeview utilizando CSS
    estilo.configure("Custom.Treeview", background="red", foreground="black", font=('Arial', 12))

    #Tabla de datos
    tabla_err = ttk.Treeview(ventana_error, columns=("Elemento1", "Elemento2", "Elemento3", "Elemento4", "Elemento5"), style="Custom.Treeview")
    tabla_err.column("#0", width=0)
    tabla_err.column("Elemento1", width=100, anchor=CENTER)
    tabla_err.column("Elemento2", width=300, anchor=CENTER)
    tabla_err.column("Elemento3", width=100, anchor=CENTER)
    tabla_err.column("Elemento4", width=100, anchor=CENTER)
    tabla_err.column("Elemento5", width=100, anchor=CENTER)

    tabla_err.heading("Elemento1", text='Token', anchor=CENTER)
    tabla_err.heading("Elemento2", text='Descripción', anchor=CENTER)
    tabla_err.heading("Elemento3", text='Tipo', anchor=CENTER)
    tabla_err.heading("Elemento4", text='Linea', anchor=CENTER)
    tabla_err.heading("Elemento5", text='Columna', anchor=CENTER)

    #Función Lógica
    #aux_error = scannergg.obtener_lista_error()
    #nuevo = []
    #aux_tac = scannergg.obtener_lista_err_sintactico()
    #sintactico = []
#
    #for i in aux_error:
    #    nuevo.append((i.caracter, i.descripcion, i.tipo, i.line, i.colum))
#
    #for j in nuevo:
    #    tabla_err.insert("", tk.END, values=j)
    #    
    ##Errores Sintácticos
    #for sintac in aux_tac:
    #    sintactico.append((sintac.caracter, sintac.descripcion, sintac.tipo, sintac.line, sintac.colum))
    #
    #for err in sintactico:
    #    tabla_err.insert("", tk.END, values=err)
    
    tabla_err.pack()
    tabla_err.place(x=40, y=30)

    ventana_error.mainloop()


#============================== Menú Principal ==============================
ventana = tkinter.Tk()
ventana.title("Text-Editor")
ventana.resizable(0, 0)
ventana.geometry("1366x768")
ventana.config(bg="black", relief="raised")
ventana.config(bd=30)

#Variables para la posición "x" y "y"
posx= StringVar()
posy = StringVar()

SubMenu = Menu(ventana, selectcolor='green')
ventana.config(menu=SubMenu)
# Items del menú1
archivo_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Nuevo", command=nuevo, font=("Courier 10 bold"), background="#F7F7F7")
archivo_menu.add_separator()
archivo_menu.add_command(label="Abrir", command=abrir, font=("Courier 10 bold"), background="#F7F7F7")
archivo_menu.add_separator()
archivo_menu.add_command(label="Guardar", command=guardar, font=("Courier 10 bold"), background="#F7F7F7")
archivo_menu.add_separator()
archivo_menu.add_command(label="Guardar Como", command=guardar_como, font=("Courier 10 bold"), background="#F7F7F7")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", font=("Courier 10 bold"), background="#F7F7F7", command=ventana.quit)
# Items del menú2
ayuda_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Análisis", menu=ayuda_menu)
ayuda_menu.add_command(label="Generar Página Web", command=analisis, font=("Courier 10 bold"), background="#F7F7F7")
#Items del menú3
tokens_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Ver Tokens", menu=tokens_menu)
tokens_menu.add_command(label="Tokens", command=ventana_mostrar_token, font=("Courier 10 bold"), background="#F7F7F7")
#Items del menú4
errores_menu = Menu(SubMenu, tearoff=0)
SubMenu.add_cascade(label="Errores", menu=errores_menu)
errores_menu.add_command(label="Errores", command=ventana_mostrar_error, font=("Courier 10 bold"), background="#F7F7F7")

#Label1
niuLabelx = Label(ventana,text="Linea:",fg="white",font=("Courier 10 bold"),bg='black')
niuLabelx.place(x=0,y=10)
#Label2
niuLabely = Label(ventana,text="Columna:",fg="white",font=("Courier 10 bold"),bg='black')
niuLabely.place(x=0,y=40)

#Label3
niuLabeln1 = Label(ventana,fg="white",font=("Courier 11 bold"),bg='black',textvariable=posx)
niuLabeln1.place(x=67,y=11)

#Label4
niuLabeln2 = Label(ventana,fg="white",font=("Courier 11 bold"),bg='black',textvariable=posy)
niuLabeln2.place(x=67,y=41)

#Función para las Posiciones (x, y)
def posicion_x_y(event):
    global posx
    global posy

    xy = scroll.index(INSERT)
    nuevo = xy.split('.')
    posx.set(nuevo[0])
    posy.set(nuevo[1])

    print('Cordenada x: ', posx, 'Cordenada y: ', posy)

scroll = scrolledtext.ScrolledText(ventana, width=140, height=40)
scroll.place(x=100, y=10)
scroll.bind("<Button-1>", posicion_x_y)
scroll.configure(bg='#000111', foreground='#16F307', font=('Courier', 10, 'bold'), wrap=WORD)
scroll.focus()
ventana.mainloop()