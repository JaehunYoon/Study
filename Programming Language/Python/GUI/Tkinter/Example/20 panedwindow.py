import tkinter

window=tkinter.Tk()
window.title("20 PanedWindow")
window.geometry("640x400+100+100")
window.resizable(True, True)

panedwindow1=tkinter.PanedWindow(relief="raised", bd=2)
panedwindow1.pack(expand=True)
 
left=tkinter.Label(panedwindow1, text="내부윈도우-1 (좌측)")
panedwindow1.add(left)

panedwindow2=tkinter.PanedWindow(panedwindow1, orient="vertical", relief="groove", bd=3)
panedwindow1.add(panedwindow2)

right=tkinter.Label(panedwindow1, text="내부윈도우-2 (우측)")
panedwindow1.add(right)

top=tkinter.Label(panedwindow2, text="내부윈도우-3 (상단)")
panedwindow2.add(top)

bottom=tkinter.Label(panedwindow2, text="내부윈도우-4 (하단)")
panedwindow2.add(bottom)

window.mainloop()