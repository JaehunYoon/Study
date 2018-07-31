import tkinter

window=tkinter.Tk()
window.title("16 ScrollBar")
window.geometry("640x400+100+100")
window.resizable(False, False)

frame=tkinter.Frame(window)

scrollbar=tkinter.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox=tkinter.Listbox(frame, yscrollcommand = scrollbar.set)
for line in range(1,1001):
   listbox.insert(line, str(line) + "/1000")
listbox.pack(side="left")

scrollbar["command"]=listbox.yview

frame.pack()

window.mainloop()