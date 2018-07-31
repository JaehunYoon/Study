import tkinter

window=tkinter.Tk()
window.title("09 MenuButton")
window.geometry("640x400+100+100")
window.resizable(False, False)

menubutton=tkinter.Menubutton(window,text="메뉴 메뉴버튼", relief="raised", direction="right")
menubutton.pack()

menu=tkinter.Menu(menubutton, tearoff=0)
menu.add_command(label="하위메뉴-1")
menu.add_separator()
menu.add_command(label="하위메뉴-2")
menu.add_command(label="하위메뉴-3")

menubutton["menu"]=menu

window.mainloop()