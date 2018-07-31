import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("27 ProgressBar")
window.geometry("640x400+100+100")
window.resizable(False, False)

progressbar=tkinter.ttk.Progressbar(window, maximum=100, mode="determinate")  # indeterminate
progressbar.pack()

progressbar.start(50)

window.mainloop()