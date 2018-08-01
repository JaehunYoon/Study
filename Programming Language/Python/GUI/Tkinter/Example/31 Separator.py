import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("31 Separator")
window.geometry("640x480+100+100")
window.resizable(False, False)

button1=tkinter.Button(window, width=10, height=5, text="1번")
button1.grid(row=0, column=0)

button2=tkinter.Button(window, width=10, height=5, text="2번")
button2.grid(row=0, column=2)

button3=tkinter.Button(window, width=10, height=5, text="3번")	
button3.grid(row=1, column=1)
		
button4=tkinter.Button(window, width=10, height=5, text="4번")
button4.grid(row=2, column=0)
		
button5=tkinter.Button(window, width=10, height=5, text="5번")
button5.grid(row=2, column=2)

s=tkinter.ttk.Separator(window, orient="vertical")	
s.grid(row=0,column=1, sticky='ns')

s2=tkinter.ttk.Separator(window, orient="horizontal")	
s2.grid(row=1,column=2, sticky='ew')

s3=tkinter.ttk.Separator(window, orient="vertical")
s3.grid(row=1,column=0, sticky='ns')

window.mainloop()x