import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("30 TreeView")
window.geometry("640x400+100+100")
window.resizable(True, True)

def cc(self):
    treeview.tag_configure("selected", background="red")

treeview=tkinter.ttk.Treeview(window, columns=["one", "two"])
treeview.pack()

treeview.column("#0", width=70)
treeview.heading("#0", text="Most")

treeview.column("one", width=100, anchor="center")
treeview.heading("one", text="챔피언", anchor="center")

treeview.column("#2", width=100, anchor="center")
treeview.heading("two", text="승률", anchor="center")

treelist=[("Zoe", "65%"), ("Leblanc", "66%"), ("Azir", "59%"), ("Lee sin", "71%"), ("Ashe", "90%")]

# print(treelist[0][0])

for i in range(len(treelist)):
    treeview.insert('', 'end', text=i, values=treelist[i])

top = treeview.insert('', 'end', text=str(len(treelist)), tags="tag1")
top_mid1 = treeview.insert(top, 'end', text="5-1", values=["one", 0])
top_mid2 = treeview.insert(top, 'end', text="5-2", values=["two", 1], tags="selected")
top_mid3 = treeview.insert(top, 'end', text="5-3", values=["three", 2])

treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=cc)

window.mainloop()