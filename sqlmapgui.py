import Tkinter
import os

#Ejecutar en la misma shell
def current():
    #global val_tampers
    payload=sqlmap+" -u "+target.get()+" -D "+db.get()+" -T "+table.get()+" -C "+column.get()+" --dump"
    print payload
    #os.system(payload)

#Funcion para abrir shells en diferentes sessiones
def other():
    payload=sqlmap+" -u "+target.get()+" -D "+db.get()+" -T "+table.get()+" -C "+column.get()+" --dump"
    #gnome-terminal -x bash -c "comando;bash"
    os.system('gnome-terminal -x bash -c "'+payload+';bash"')

def set_tamp(var):
    #global var
    #i = 0
    #for i in range (0,len(val_tampers)-1):
    #    print str(val_tampers[i].get())+",",
    #print ""
    print var
    
def tampers():
    tamperv = Tkinter.Tk()
    tamperv.title("Window-Tampers")
    x=root.winfo_x()#+400
    y=root.winfo_y()+300
    #tamperv.overrideredirect(1)
    tamperv.geometry("600x330+"+str(x)+"+"+str(y))
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

    current_tampers=[]

    tamp_info = Tkinter.Button(tamperv, text="Que tamper usar", command=tamp_txt)
    tamp_info.grid(row=0,column=0)

    #var = Tkinter.IntVar()
    #chk = Tkinter.Checkbutton(tamperv, text="checkbox", variable=var,  command=lambda:set_tamp(var))
    #chk.grid(row=0,column=1)
    #chk.select()

    #tamp_info = Tkinter.Button(tamperv, text="Actualizar Tampers", command=lambda: set_tamp(var))
    #tamp_info.grid(row=0,column=2)

    r = 1
    c = 0
    pos = 0
    #val_tampers = []
    for tamper in tampers:
        #print pos
        #val_tampers.append(Tkinter.IntVar())
        Tkinter.Checkbutton(tamperv, text=tamper, command=lambda:set_tamp(str(tamper))).grid(row=r,column=c)
        print tampers[pos]
        pos = pos + 1
        #c = c + 1
        r = r + 1
        if r == 14:
            #c = 0
            #r = r + 1
            r = 1
            c = c + 1

    tamperv.mainloop()
    #if tamp == 0:
    #    tamperv.state(newstate='normal')
    #    btn_text.set("Ocultar Window Tamper")
    #    tamp = 1
    #else:
    #    tamperv.state(newstate='withdraw')
    #    btn_text.set("Mostrar Window Tamper")
    #    tamp = 0

def tamp_txt():
    os.system('gnome-terminal -x bash -c "cat tampers.txt;bash"')
   
   
#####################################################    
#Ventana main
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

########################################################
#Ventana Tamper

#tamperv = Tkinter.Tk()
#tamperv.title("Window-Tampers")
#tamperv.geometry("500x300")
#tamperv.overrideredirect(1)
#tamperv.state(newstate='withdraw')




"""
r = 1
c = 0
pos = 0
val_tampers = []
for tamper in tampers:
    #print pos
    val_tampers.append(Tkinter.IntVar())
    Tkinter.Checkbutton(tamperv, text=tamper, variable=val_tampers[pos]).grid(row=r,column=c)
    pos = pos + 1
    #c = c + 1
    r = r + 1
    if r == 14:
        #c = 0
        #r = r + 1
        r = 1
        c = c + 1
"""


#Loop infinito hasta cerrar la ventana
root.mainloop()