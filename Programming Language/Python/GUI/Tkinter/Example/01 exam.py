import tkinter

window = tkinter.Tk()

window.title("01 Tkinter GUI Example")
window.geometry("640x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window, text="Hello World!")
label.pack()

window.mainloop()