import tkinter

window=tkinter.Tk()
window.title("13 frame")
window.geometry("640x400+100+100")
window.resizable(False, False)

frame1=tkinter.Frame(window, relief="solid", bd=2)
frame1.pack(side="left", fill="both", expand=True)

frame2=tkinter.Frame(window, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

button1=tkinter.Button(frame1, text="프레임1")
button1.pack(side="right")

button2=tkinter.Button(frame2, text="프레임2")
button2.pack(side="left")

window.mainloop()