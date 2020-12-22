from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox 

def nuevo():

    if len(texto.get("1.0", "end-1c")) != 0:

        respuesta = MessageBox.askquestion("Atención", "¿Desea guardar el texto actual?")

        if respuesta == "yes":
            guardado = guardarComo()
            if guardado:
                texto.delete('1.0', END)
                label.config(text="Bienvenido a tu editor de texto plano")
        else:
            texto.delete('1.0', END)
            label.config(text="Bienvenido a tu editor de texto plano")

def abrir():
    fichero = FileDialog.askopenfilename(
        initialdir="/C:", 
        filetypes=(("Archivos de texto","*.txt"),), 
        title = "Seleccionar fichero" )
    if fichero != "":
        contFichero = open(fichero, "r", encoding="utf-8")
        textArchivo = contFichero.read()
        contFichero.close()
        nuevo()
        texto.insert('1.0', textArchivo)
        label.config(text=fichero)

def guardar():
    if label['text'] != "Bienvenido a tu editor de texto plano":
        fichero = open(label['text'], 'w+')
        fichero.write(texto.get('1.0', END))
        fichero.close()
        info = MessageBox.showinfo("Información", "Fichero guardado")
    else:
        guardarComo()

def guardarComo():
    fichero = FileDialog.asksaveasfilename(
        initialdir="/C:", 
        defaultextension=".txt", 
        filetypes=(("Archivos de texto","*.txt"),), 
        title = "Guardar como" )
    if fichero != "":
        contFichero = open(fichero, "w", encoding="utf-8")
        contFichero.write(texto.get('1.0', END))
        contFichero.close()
        label.config(text=fichero)
        info = MessageBox.showinfo("Información", "Fichero guardado")
    return fichero

root = Tk()

root.title("Txt Editor")

menubar = Menu(root)
root.config(menu=menubar)

archivo = Menu(menubar, tearoff=0)
archivo.add_command(label="Nuevo", command=nuevo)
archivo.add_command(label="Abrir", command=abrir)
archivo.add_command(label="Guardar", command=guardar)
archivo.add_command(label="Guardar como", command=guardarComo)
archivo.add_separator()
archivo.add_command(label="Salir", command=root.quit)

menubar.add_cascade(label="Archivo", menu=archivo)

texto = Text(root)
texto.pack(expand=1, fill=BOTH)
texto.config(font=("Consolas",12), padx=15, pady=15)

label = Label(root,text="Bienvenido a tu editor de texto plano")
label.pack()

root.mainloop()
