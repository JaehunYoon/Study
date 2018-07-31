import tkinter

window=tkinter.Tk()
window.title("11 place")
window.geometry("640x400+100+100")
window.resizable(False, False)

b1=tkinter.Button(window, text="(50, 50)")
b2=tkinter.Button(window, text="(50, 100)")
b3=tkinter.Button(window, text="(100, 150)")
b4=tkinter.Button(window, text="(0, 200)")
b5=tkinter.Button(window, text="(0, 300)")
b6=tkinter.Button(window, text="(0, 300)")

b1.place(x=50, y=50)
b2.place(x=50, y=100, width=50, height=50)
b3.place(x=100, y=150, bordermode="inside")
b4.place(x=0, y=200, relwidth=0.5)
b5.place(x=0, y=300, relx=0.5)
b6.place(x=0, y=300, relx=0.5, anchor="s")

window.mainloop()