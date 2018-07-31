import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("28 notebook")
window.geometry("640x400+100+100")
window.resizable(False, False)

notebook=tkinter.ttk.Notebook(window, width=300, height=300)
notebook.pack()

frame1=tkinter.Frame(window)
notebook.add(frame1, text="페이지1")

label1=tkinter.Label(frame1, text="떡볶이 먹고싶다.")
label1.pack()

frame2=tkinter.Frame(window)
notebook.add(frame2, text="페이지2")

label2=tkinter.Label(frame2, text="오늘은 떡볶이를 먹었다.")
label2.pack()

frame3=tkinter.Frame(window)
notebook.add(frame3, text="페이지4")

label3=tkinter.Label(frame3, text="개구리")
label3.pack()

frame4=tkinter.Frame(window)
notebook.insert(2, frame4, text="페이지3")

label4=tkinter.Label(frame4, text="올챙이")
label4.pack()

window.mainloop()