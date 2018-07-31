import tkinter

window = tkinter.Tk()

window.title("02 Tkinter Label Example")
window.geometry("1280x1080")
window.resizable(False, False)

flat = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="flat")
flat.pack()

groove = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="groove")
groove.pack()

raised = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="raised")
raised.pack()

ridge = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="raised")
ridge.pack()

solid = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="solid")
solid.pack()

sunken = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="sunken")
sunken.pack()

# ridge = tkinter.Label(window, text="Hello World!", width=10, height=5, fg="red", relief="raised")
# ridge.pack()

window.mainloop()