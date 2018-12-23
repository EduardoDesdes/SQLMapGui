import Tkinter
import os

#Funcion para ejecutar el sqlmap en la misma shell que se ejecuta el programa
def current():
    #global val_tampers
    payload=sqlmap+" -u "+target.get()+" -D "+db.get()+" -T "+table.get()+" -C "+column.get()+" --dump"
    #Verificar antes de ejecutar
    print payload
    #Ejecutar en la shell
    #os.system(payload)

#Funcion para ejecutar el sqlmap en otras shells
def other():
    payload=sqlmap+" -u "+target.get()+" -D "+db.get()+" -T "+table.get()+" -C "+column.get()+" --dump"
    #Comando usado: gnome-terminal -x bash -c "comando;bash"
    os.system('gnome-terminal -x bash -c "'+payload+';bash"')

#Funcion para crear la cadena de tampers ejm: tamper1,tamper2,tamper3
def set_tamp(var):
    #global var
    #i = 0
    #for i in range (0,len(val_tampers)-1):
    #    print str(val_tampers[i].get())+",",
    #print ""
    print var
#Ventana Window Tamper    
def tampers():

    #Creaccion de la ventana tamper
    tamperv = Tkinter.Tk()
    tamperv.title("Window-Tampers")
    #seteando posicion con la ventana main
    x=root.winfo_x()#+400
    y=root.winfo_y()+300
    tamperv.geometry("600x330+"+str(x)+"+"+str(y))
    #Quitando Bordes
    #tamperv.overrideredirect(1)

    #Tamper List
    tampers=["apostrophemask","apostrophenullencode","appendnullbyte",
        "base64encode","between","bluecoat","chardoubleencode",
        "charencode","charunicodeencode","concat2concatws",
        "equaltolike","greatest","halfversionedmorekeywords",
        "ifnull2ifisnull","modsecurityversioned","modsecurityzeroversioned",
        "multiplespaces","nonrecursivereplacement","percentage",
        "randomcase","randomcomments","securesphere","space2comment",
        "space2dash","space2hash","space2morehash","space2mssqlblank",
        "space2mssqlhash","space2mysqlblank","space2mysqldash",
        "space2plus","space2randomblank","sp_password","unionalltounion",
        "unmagicquotes","versionedkeywords","versionedmorekeywords"]

    #Tamper Seleccionados
    current_tampers=[]

    #Boton informativo
    tamp_info = Tkinter.Button(tamperv, text="Que tamper usar", command=tamp_txt)
    tamp_info.grid(row=0,column=0)

    #var = Tkinter.IntVar()
    #chk = Tkinter.Checkbutton(tamperv, text="checkbox", variable=var,  command=lambda:set_tamp(var))
    #chk.grid(row=0,column=1)
    #chk.select()

    #tamp_info = Tkinter.Button(tamperv, text="Actualizar Tampers", command=lambda: set_tamp(var))
    #tamp_info.grid(row=0,column=2)

    #Agregar los Checkbutton en la ventana tamper
    r = 1
    c = 0
    pos = 0
    cb_tampers = []
    for tamper in tampers:
        #print pos
        #val_tampers.append(Tkinter.IntVar())
        Tkinter.Checkbutton(tamperv, text=tamper, command=lambda:set_tamp()).grid(row=r,column=c)
        print tampers[pos]
        pos = pos + 1
        #c = c + 1
        r = r + 1
        if r == 14:
            #c = 0
            #r = r + 1
            r = 1
            c = c + 1

    #Loop Ventana tampers
    tamperv.mainloop()

    #Para validad y actualizar el texto del boton del tamper
    #if tamp == 0:
    #    tamperv.state(newstate='normal')
    #    btn_text.set("Ocultar Window Tamper")
    #    tamp = 1
    #else:
    #    tamperv.state(newstate='withdraw')
    #    btn_text.set("Mostrar Window Tamper")
    #    tamp = 0

#Ejecutar lista de tampers informativa
def tamp_txt():
    os.system('gnome-terminal -x bash -c "cat tampers.txt;bash"')
   
   
#####################################################    
#Ventana Principal
root = Tkinter.Tk()
root.title("SqlMapGui")
root.geometry("400x300")

#Creando cadena inicial

sqlmap = "sqlmap"

#Target
Tkinter.Label(root, text="Ingrese la url").pack()
target = Tkinter.Entry()
target.pack()

#Base de Dato/s
Tkinter.Label(root, text="Ingrese la base de datos").pack()
db = Tkinter.Entry()
db.pack()

#Tabla/s
Tkinter.Label(root, text="Ingrese la tabla").pack()
table = Tkinter.Entry()
table.pack()

#Columna/s
Tkinter.Label(root, text="Ingrese la columna").pack()
column = Tkinter.Entry()
column.pack()

#Dump
Tkinter.Label(root, text="Dump").pack()



#Boton para entrar a la funcion
boton1 = Tkinter.Button(root, text="Ejecutar en la misma ventana", command=current)
boton1.pack()

boton2 = Tkinter.Button(root, text="Ejecutar en otra ventana", command=other)
boton2.pack()

#Deslizar ventana tampers
btn_text = Tkinter.StringVar()
boton3 = Tkinter.Button(root, textvariable=btn_text, command=tampers)
btn_text.set("Mostrar Window Tamper")
boton3.pack()
tamp = 0

#Loop infinito hasta cerrar la ventana
root.mainloop()