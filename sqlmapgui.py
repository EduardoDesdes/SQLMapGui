#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import os

#Funcion para ejecutar el sqlmap en la misma shell que se ejecuta el programa
def current(val = 1):
    
    #global val_tampers
    payload=sqlmap

    if target.get() is not "":
        payload = payload + " -u \""+target.get()

        if post.get('1.0', 'end-1c') is not "":
            payload = payload + "\" --data \""+post.get('1.0', 'end-1c')

        if parametros.get() is not "":
            payload = payload + "\" -p \""+parametros.get()

        if db.get() is not "":
            payload = payload + "\" -D \""+db.get()

            if table.get() is not "":
                payload = payload + "\" -T \""+table.get()

                if column.get() is not "":
                    payload = payload +"\" -C \""+column.get()+"\" --dump"
                else:
                    payload = payload + "\" --columns"
            else:
                payload = payload + "\" --tables"
        else:
            payload = payload + "\" --dbs"
    else:
        payload = payload + " --h"

    if lvl.get() is not "":
        payload = payload + " --level="+lvl.get()
    if rsk.get() is not "":
        payload = payload + " --risk="+rsk.get()
    if thr.get() is not "":
        payload = payload + " --threads="+thr.get()
    if v.get() is not "":
        payload = payload + " -v "+v.get()
    #no-cast
    if nc.get() is 1:
        payload = payload + " --no-cast"
    #random-agent
    if ra.get() is 1:
        payload = payload + " --random-agent"
    #user-agent
    if ua.get() is not "":
        payload = payload + " --user-agent=\""+ua.get()+"\""
    #timesec
    if ts.get() is not "":
        payload = payload + " --time-sec="+ts.get()
    #timeout
    if to.get() is not "":
        payload = payload + " --timeout="+to.get()
    #proxy
    if proxy.get() is not "":
        payload = payload + " --proxy=\""+proxy.get()+"\""

    #Guardando logs
    #log.write(payload+'\n')
    #log.close()
    
    if val == 1:
        #Iniciando archivo de logs
        log = open ('logsqlmapgui.txt','a')
        #Verificar antes de ejecutar
        print payload
        #Guardando logs
        log.write(payload+'\n')
        log.close()
        #Ejecutar en la shell
        os.system(payload)
    else:
        return payload
    #Cerrando los logs

#Funcion para ejecutar el sqlmap en otras shells
def other():
    #global current_tampers
    #Obteniendo el payload de la funcion current
    payl = current(0)
    #print payl
    #print current_tampers
    if len(current_tampers) is not 0:
        for tamper in current_tampers:
            #Iniciando archivo de logs
            log = open ('logsqlmapgui.txt','a')
            #Creando comando con tampers
            comand = payl+" --tamper=\""+tamper+"\""
            #Guardando logs
            log.write(comand+'\n')
            log.close()
            #Ejecutando
            os.system('gnome-terminal -x bash -c "'+comand+';bash"')
    else:
        #Iniciando archivo de logs
        log = open ('logsqlmapgui.txt','a')
        log.write(payl+'\n')
        log.close()
        os.system('gnome-terminal -x bash -c "'+payl+';bash"')
    #Comando usado: gnome-terminal -x bash -c "comando;bash"
    #os.system('gnome-terminal -x bash -c "'+payload+';bash"')

#Funcion para crear la cadena de tampers ejm: tamper1,tamper2,tamper3
def set_tamp(var):
    if var in current_tampers:
        current_tampers.remove(var)
    else:
        current_tampers.append(var)

    #print current_tampers
#Ventana Window Tamper    
def tampers():

    #Creaccion de la ventana tamper
    tamperv = Tkinter.Tk()
    tamperv.title("Window-Tampers")
    #seteando posicion con la ventana main
    x=root.winfo_x()+400
    y=root.winfo_y()#+300
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

    #Boton informativo
    tamp_info = Tkinter.Button(tamperv, text="Que tamper usar", command=tamp_txt)
    tamp_info.grid(row=0,column=1)


    #Agregar los Checkbutton en la ventana tamper (No funcionó >:v)
    """
    r = 1
    c = 0
    pos = 0
    cb_tampers = []
    for tamper in tampers:
        #print pos
        #val_tampers.append(Tkinter.IntVar())
        Tkinter.Checkbutton(tamperv, text=tamper, command=lambda:set_tamp(self.get("text"))).grid(row=r,column=c)
        print tampers[pos]
        pos = pos + 1
        #c = c + 1
        r = r + 1
        if r == 14:
            #c = 0
            #r = r + 1
            r = 1
            c = c + 1
    """
    #Alv asi si funciona xd

    Tkinter.Checkbutton(tamperv, text=tampers[0], command=lambda:set_tamp(tampers[0])).grid(row=1,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[1], command=lambda:set_tamp(tampers[1])).grid(row=2,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[2], command=lambda:set_tamp(tampers[2])).grid(row=3,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[3], command=lambda:set_tamp(tampers[3])).grid(row=4,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[4], command=lambda:set_tamp(tampers[4])).grid(row=5,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[5], command=lambda:set_tamp(tampers[5])).grid(row=6,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[6], command=lambda:set_tamp(tampers[6])).grid(row=7,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[7], command=lambda:set_tamp(tampers[7])).grid(row=8,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[8], command=lambda:set_tamp(tampers[8])).grid(row=9,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[9], command=lambda:set_tamp(tampers[9])).grid(row=10,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[10], command=lambda:set_tamp(tampers[10])).grid(row=11,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[11], command=lambda:set_tamp(tampers[11])).grid(row=12,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[12], command=lambda:set_tamp(tampers[12])).grid(row=13,column=0)
    Tkinter.Checkbutton(tamperv, text=tampers[13], command=lambda:set_tamp(tampers[13])).grid(row=1,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[14], command=lambda:set_tamp(tampers[14])).grid(row=2,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[15], command=lambda:set_tamp(tampers[15])).grid(row=3,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[16], command=lambda:set_tamp(tampers[16])).grid(row=4,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[17], command=lambda:set_tamp(tampers[17])).grid(row=5,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[18], command=lambda:set_tamp(tampers[18])).grid(row=6,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[19], command=lambda:set_tamp(tampers[19])).grid(row=7,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[20], command=lambda:set_tamp(tampers[20])).grid(row=8,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[21], command=lambda:set_tamp(tampers[21])).grid(row=9,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[22], command=lambda:set_tamp(tampers[22])).grid(row=10,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[23], command=lambda:set_tamp(tampers[23])).grid(row=11,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[24], command=lambda:set_tamp(tampers[24])).grid(row=12,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[25], command=lambda:set_tamp(tampers[25])).grid(row=13,column=1)
    Tkinter.Checkbutton(tamperv, text=tampers[26], command=lambda:set_tamp(tampers[26])).grid(row=1,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[27], command=lambda:set_tamp(tampers[27])).grid(row=2,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[28], command=lambda:set_tamp(tampers[28])).grid(row=3,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[29], command=lambda:set_tamp(tampers[29])).grid(row=4,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[30], command=lambda:set_tamp(tampers[30])).grid(row=5,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[31], command=lambda:set_tamp(tampers[31])).grid(row=6,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[32], command=lambda:set_tamp(tampers[32])).grid(row=7,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[33], command=lambda:set_tamp(tampers[33])).grid(row=8,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[34], command=lambda:set_tamp(tampers[34])).grid(row=9,column=2)
    Tkinter.Checkbutton(tamperv, text=tampers[35], command=lambda:set_tamp(tampers[35])).grid(row=10,column=2)
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

def logsqlmap():
     os.system('gnome-terminal -x bash -c "cat logsqlmapgui.txt;bash"')  
   
#####################################################    
#Ventana Principal
root = Tkinter.Tk()
root.title("SqlMapGui")
root.geometry("400x400")

#Creando cadena inicial

sqlmap = "sqlmap"

#InterfaceGrafica
Tkinter.Label(root, text="------Target Section---------------------------------------------------").place(x=10, y=5)
#Target
Tkinter.Label(root, text="URL Vulnerable").place(x=15, y=25)
target = Tkinter.Entry(root, width=45)
target.place(x=15, y=40)

#PostDate
Tkinter.Label(root, text="Data Post").place(x=15, y=65)
post = Tkinter.Text(root, height=2, width=45)
post.place(x=15, y=80)

#Parametros
Tkinter.Label(root, text="Parametros").place(x=15, y=125)
parametros = Tkinter.Entry(root, width=20)
parametros.place(x=15, y=140)

#Base de Dato/s
Tkinter.Label(root, text="Base de Datos").place(x=215, y=125)
db = Tkinter.Entry()
db.place(x=215, y=140)

#Tabla/s
Tkinter.Label(root, text="Ingrese la tabla").place(x=15, y=165)
table = Tkinter.Entry()
table.place(x=15, y=180)

#Columna/s
Tkinter.Label(root, text="Ingrese la columna").place(x=215, y=165)
column = Tkinter.Entry()
column.place(x=215, y=180)

#Level
Tkinter.Label(root, text="--level=").place(x=15, y=205)
lvl = Tkinter.Entry(root, width=1)
lvl.place(x=70, y=205)

#Risk
Tkinter.Label(root, text="--risk=").place(x=95, y=205)
rsk = Tkinter.Entry(root, width=1)
rsk.place(x=140, y=205)

#Threads
Tkinter.Label(root, text="--threads=").place(x=160, y=205)
thr = Tkinter.Entry(root, width=2)
thr.place(x=230, y=205)

#Verbosidad 
Tkinter.Label(root, text="-v").place(x=252, y=205)
v = Tkinter.Entry(root, width=1)
v.place(x=270, y=205)

#No Cast
nc = Tkinter.IntVar()
Tkinter.Checkbutton(root, text="--no-cast", variable=nc).place(x=290, y=205)

Tkinter.Label(root, text="------Connection Section---------------------------------------------").place(x=10, y=230)

#--Random-Agent
ra = Tkinter.IntVar()
Tkinter.Checkbutton(root, text="--random-agent", variable=ra).place(x=8, y=250)

#--user-agent=
Tkinter.Label(root, text="--user-agent=").place(x=140, y=250)
ua = Tkinter.Entry(root, width=18)
ua.place(x=233, y=250)

#Time Sec
Tkinter.Label(root, text="--time-sec=").place(x=10, y=275)
ts = Tkinter.Entry(root, width=2)
ts.place(x=88, y=275)


#TimeOUT
Tkinter.Label(root, text="--timeout=").place(x=110, y=275)
to = Tkinter.Entry(root, width=2)
to.place(x=185, y=275)

#Proxy
Tkinter.Label(root, text="--proxy=").place(x=210, y=275)
proxy = Tkinter.Entry(root, width=13)
proxy.place(x=273, y=275)


#Tamper Seleccionados
current_tampers=[]

Tkinter.Label(root, text="------Extra Section---------------------------------------------").place(x=10, y=300)


#Boton para entrar a la funcion
boton1 = Tkinter.Button(root, text="Run SQLMAP current Shell", command=current)
boton1.place(x=5, y=320)

boton2 = Tkinter.Button(root, text="Run SQLMAP other Shell", command=other)
boton2.place(x=210, y=320)

#Deslizar ventana tampers
btn_text = Tkinter.StringVar()
boton3 = Tkinter.Button(root, textvariable=btn_text, command=tampers)
btn_text.set("Seleccionar algun Tamper")
boton3.place(x=5, y=355)
tamp = 0

#Registro de comandos SQLMAP
boton2 = Tkinter.Button(root, text="SqlMap History Payload", command=logsqlmap)
boton2.place(x=210, y=355)

#Loop infinito hasta cerrar la ventana
root.mainloop()