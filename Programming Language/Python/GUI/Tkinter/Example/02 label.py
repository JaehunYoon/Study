import tkinter

window = tkinter.Tk()

window.title("01 Tkinter GUI Example")
window.geometry("640x400+100+100")
window.resizable(False, False)

flat = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="flat")
flat.pack()

groove = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="groove")
groove.pack()

raised = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="raised")
raised.pack()
window.mainloop()