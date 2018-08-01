import tkinter as tk

def window1():
    window = tk.Toplevel(root)
    window.title("Welcome")

    # etc etc ...

    tk.Button(window,text="Enter...",command=lambda: window2(window)).pack()

def window2(old_window):
    old_window.destroy()
    # window2 stuff

root = tk.Tk()
root.iconify() # to minimize it, since we're just using Toplevels on top of it
window1()
root.mainloop()