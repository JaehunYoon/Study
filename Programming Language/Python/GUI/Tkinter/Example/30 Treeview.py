import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("30 TreeView")
window.geometry("640x400+100+100")
window.resizable(False, False)

def cc(self):
    treeview.tag_configure("tag2", background="red")

treeview=tkinter.ttk.Treeview(window, columns=["one", "two"], displaycolumns=["two", "one"])
treeview.pack()

treeview.column("#0", width=70)
treeview.heading("#0", text="num")

treeview.column("one", width=100, anchor="center")
treeview.heading("one", text="문자", anchor="e")

treeview.column("#2", width=100, anchor="w")
treeview.heading("two", text="ASCII", anchor="center")

treelist=[("A", 65), ("B", 66), ("C", 67), ("D", 68), ("E", 69)]

for i in range(len(treelist)):
    
    treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i)+"번")

top=treeview.insert('', 'end', text=str(len(treelist)), iid="5번", tags="tag1")
top_mid1=treeview.insert(top, 'end', text="5-2", values=["SOH", 1], iid="5번-1")
top_mid2=treeview.insert(top, 0, text="5-1", values=["NUL", 0], iid="5번-0", tags="tag2")
top_mid3=treeview.insert(top, 'end', text="5-3", values=["STX", 2], iid="5번-2", tags="tag2")

treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=cc)

window.mainloop()