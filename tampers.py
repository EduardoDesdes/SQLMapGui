r = 1
c = 0

for i in range (0,37):
	print "Tkinter.Checkbutton(tamperv, text=tampers["+str(i)+"], command=lambda:set_tamp(tampers["+str(i)+"])).grid(row="+str(r)+",column="+str(c)+")"
	r = r + 1

	if r == 14:
		#c = 0
		#r = r + 1
		r = 1
		c = c + 1
