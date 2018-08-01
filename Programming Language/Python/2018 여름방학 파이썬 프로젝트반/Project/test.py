import requests
import tkinter
import tkinter.ttk
from urllib.parse import quote
from bs4 import BeautifulSoup
from func import *
from time import sleep

__author__ = "goodasd123@naver.com"
__github__ = "https://github.com/JaehunYoon/"

# Window Initiallize
window = tkinter.Tk()
window.title("Simple OP.GG")
window.geometry("640x800")
# window.state("zoomed")
window.resizable(True, True)

# Menu
menubar = tkinter.Menu(window)
menu = tkinter.Menu(menubar, tearoff=0)
menu.add_command(label="h4lo")
menu.add_command(label="h4lo")
menu.add_separator()
menu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label="메뉴", menu=menu)
window.config(menu=menubar)

# Frame, ScrollBar
frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side='right', fill="y")

# Main title Image
image = tkinter.PhotoImage(file="main.PNG")
title_image = tkinter.Label(window, image=image)
title_image.pack()


def summoner_name(event):
    most_champion_list.delete(0, 'end')
    user = get_username(input_username.get())

    if user == None:
        summoner_label.config(text="OP.GG에 등록되지 않은 소환사입니다. 오타를 확인 후 다시 검색해주세요.")
        solo_rank_label.config(text='')
        flex_rank_label.config(text='')
    else:
        # Summoner's Information
        summoner_label.config(text=f"소환사명 : {user['summoner_name']}")
        if user['solo_rank_tier'] == 'Unranked':
            solo_rank_label.config(text=f"솔로랭크 : {user['solo_rank_tier']}")
        else:
            solo_rank_label.config(text=f"솔로랭크 : {user['solo_rank_tier']} {user['solo_rank_point']}")
        if user['flex_rank_tier'] == 'Unranked':
            flex_rank_label.config(text=f"자유 5:5 랭크 : {user['flex_rank_tier']}")
        else:
            flex_rank_label.config(text=f"자유 5:5 랭크 : {user['flex_rank_tier']} {user['flex_rank_point']}")

        # Most Champion
        for index, champion in enumerate(get_most_champion(input_username.get())):
            most_champion_list.insert(index + 1, f"Most {index+1} : {champion['data-value']}")

# Entry
input_username = tkinter.Entry(window)
input_username.bind("<Return>", summoner_name)
input_username.pack()

# Label
summoner_label = tkinter.Label(window)
solo_rank_label = tkinter.Label(window)
flex_rank_label = tkinter.Label(window)

# ScrollBox
most_champion_list = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
scrollbar["command"] = most_champion_list.yview

# Pack
summoner_label.pack()
solo_rank_label.pack()
flex_rank_label.pack()
most_champion_list.pack(side="left")
frame.pack()

# Sub Screen
sub_screen = tkinter.Toplevel(window)
sub_screen.geometry("640x480+700+100")

# --test--
def cc(self):
    treeview.tag_configure("selected", background="red")

treeview=tkinter.ttk.Treeview(sub_screen, columns=["one", "two"])
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
# --test--

window.mainloop()
# -----
