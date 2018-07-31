import tkinter

window=tkinter.Tk()
window.title("19 LabelFrame")
window.geometry("640x400+100+100")
window.resizable(True, True)

def check():
    label.config(text=RadioVariety_1.get())
    
labelframe=tkinter.LabelFrame(window, text="플랫폼 선택")
labelframe.pack()

RadioVariety_1=tkinter.StringVar()
RadioVariety_1.set("미선택")

radio1=tkinter.Radiobutton(labelframe, text="Python", value="가능", variable=RadioVariety_1, command=check)
radio1.pack()
radio2=tkinter.Radiobutton(labelframe, text="C/C++", value="부분 가능", variable=RadioVariety_1, command=check)
radio2.pack()
radio3=tkinter.Radiobutton(labelframe, text="JSON", value="불가능", variable=RadioVariety_1, command=check)
radio3.pack()
label=tkinter.Label(labelframe, text="None")
label.pack()

window.mainloop()