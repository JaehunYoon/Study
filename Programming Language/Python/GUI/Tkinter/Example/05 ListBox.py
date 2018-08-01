import tkinter

window=tkinter.Tk()
window.title("05 ListBox")
window.geometry("640x480+100+100")
window.resizable(False, False)

listbox = tkinter.Listbox(window, selectmode='select', height=10)
listbox.insert(0, "hi")
listbox.insert(1, "hello")
listbox.insert(2, "nice")
listbox.insert(3, "wow")
listbox.insert(4, "yeah")
listbox.delete(1, 2)
listbox.pack()

window.mainloop()