import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("29 SizeGrip")
window.geometry("640x400+100+100")
window.resizable(False, False)

def Drag(event):

    x=sizegrip.winfo_x()+event.x
    y=sizegrip.winfo_y()+event.y
    sz_width=sizegrip.winfo_reqwidth()
    sz_height=sizegrip.winfo_reqheight()

    text["width"]=x-sz_width
    text["height"]=y-sz_height

    if x >= sz_width and y >= sz_height and x < window.winfo_width() and y < window.winfo_height():
        text.place(x=0, y=0, width=x, height=y)
        sizegrip.place(x=x-sz_width, y=y-sz_height)

text=tkinter.Text(window)
text.place(x=0, y=0)

sizegrip=tkinter.ttk.Sizegrip(window)
sizegrip.place(x=text.winfo_reqwidth()-sizegrip.winfo_reqwidth() , y=text.winfo_reqheight()-sizegrip.winfo_reqheight() )
sizegrip.bind("<B1-Motion>", Drag)

window.mainloop()