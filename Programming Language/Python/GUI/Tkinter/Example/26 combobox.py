import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("26 ComboBox")
window.geometry("640x400+100+100")
window.resizable(False, False)

values=[str(i)+"번" for i in range(1, 101)] 

combobox=tkinter.ttk.Combobox(window, height=15, values=values)
combobox.pack()

combobox.set("목록 선택")

window.mainloop()