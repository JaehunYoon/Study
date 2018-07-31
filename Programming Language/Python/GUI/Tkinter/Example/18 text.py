import tkinter

window=tkinter.Tk()
window.title("17 text")
window.geometry("640x400+100+100")
window.resizable(True, True)

text=tkinter.Text(window)

text.insert(tkinter.CURRENT, "안녕하세요.\n")
text.insert("current", "반습니다.")
text.insert(2.1, "갑")

text.pack()

text.tag_add("강조", "1.0", "1.6")
text.tag_config("강조", background="yellow") 
text.tag_remove("강조", "1.1", "1.2")

window.mainloop()