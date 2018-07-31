import tkinter

window=tkinter.Tk()
window.title("24 TopLevel")
window.geometry("640x400+100+100")
window.resizable(False, False)

menubar=tkinter.Menu(window)

menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-3")
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

toplevel=tkinter.Toplevel(window, menu=menubar)
toplevel.geometry("320x200+820+100")

label=tkinter.Label(toplevel, text="h4lo")
label.pack()

window.mainloop()