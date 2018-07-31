import tkinter

window=tkinter.Tk()
window.title("15 canvas")
window.geometry("640x400+100+100")
window.resizable(False, False)

canvas=tkinter.Canvas(window, relief="solid", bd=2)

line=canvas.create_line(10, 10, 20, 20, 20, 130, 30, 140, fill="red")
polygon=canvas.create_polygon(50, 50, 170, 170, 100, 170, outline="yellow")
oval=canvas.create_oval(100, 200, 150, 250, fill="blue", width=3)
arc=canvas.create_arc(100, 100, 300, 300, start=0, extent=150, fill='red')

canvas.pack()

window.mainloop()