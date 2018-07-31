import tkinter

window=tkinter.Tk()
window.title("22 PhotoImage")
window.geometry("1280x1080")
window.resizable(True, True)

image=tkinter.PhotoImage(file="22.png")

label=tkinter.Label(window, image=image)
label.pack()

window.mainloop()