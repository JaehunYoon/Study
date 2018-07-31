import tkinter

window=tkinter.Tk()
window.title("09 Widget Pack")
window.geometry("640x400+100+100")
window.resizable(False, False)

b1=tkinter.Button(window, text="top")
b1_1=tkinter.Button(window, text="top-1")

b2=tkinter.Button(window, text="bottom")
b2_1=tkinter.Button(window, text="bottom-1")

b3=tkinter.Button(window, text="left")
b3_1=tkinter.Button(window, text="left-1")

b4=tkinter.Button(window, text="right")
b4_1=tkinter.Button(window, text="right-1")

b5=tkinter.Button(window, text="center", bg="red")

b1.pack(side="top")
b1_1.pack(side="top", fill="x")

b2.pack(side="bottom")
b2_1.pack(side="bottom", anchor="e")

b3.pack(side="left")
b3_1.pack(side="left", fill="y")

b4.pack(side="right")
b4_1.pack(side="right", anchor="s")

b5.pack(expand=True, fill="both")

window.mainloop()