import Tkinter

def valite():
	print var.get()

root = Tkinter.Tk()
root.geometry("400x300")

var = Tkinter.IntVar()
chk = Tkinter.Checkbutton(root, text='foo', variable=var,command=valite)
chk.pack()

tamp_info = Tkinter.Button(root, text="Go", command=valite)
tamp_info.pack()

root.mainloop()