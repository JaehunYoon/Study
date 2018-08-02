import requests
import tkinter
import tkinter.ttk
from urllib.parse import quote
from bs4 import BeautifulSoup
from func import *
from time import sleep

__author__ = "goodasd123@naver.com"
__github__ = "https://github.com/JaehunYoon/"

# --test--
test_champ = []
# --test--

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

temp = []

# Frame, ScrollBar
frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side='right', fill="y")

# Main title Image
image = tkinter.PhotoImage(file="main.PNG")
title_image = tkinter.Label(window, image=image)
title_image.pack()


def summoner_name(event):
    test_champ = []
    test_winrate = []
    global temp

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
            test_champ.append(champion['data-value'])
        
        # Test
        for champ in get_most_champion(input_username.get()):
            test_champ.append(champ['data-value'])

        for win in get_champion_winrate(input_username.get()):
            test_winrate.append(win.text)

        temp = list(zip(test_champ, test_winrate))

        print(temp)
        champion_winrate()

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

# ---test---

def champion_winrate():
    global temp
    # def cc(self):
    #     treeview.tag_configure("selected", background="red")
    
    sub_screen = tkinter.Toplevel(window)
    sub_screen.geometry("640x480+700+100")
    treeview = tkinter.ttk.Treeview(sub_screen, columns=["one", "two"])
    treeview.pack()

    treeview.column("#0", width=70)
    treeview.heading("#0", text="Most", anchor="center")

    treeview.column("one", width=100, anchor="center")
    treeview.heading("one", text="챔피언", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="승률", anchor="center")

    treelist = temp

    top = list(range(len(treelist)))
    top_mid = [[0 for _ in range(3)] for _ in range(len(treelist))]

    for i in range(len(treelist)):
        top[i] = treeview.insert('', 'end', text=i, values=treelist[i], tags="tag1")
        for j in range(3):
            top_mid[i][j] = treeview.insert(top[i], 'end', text="test", values=["test", j])

    treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>") # , callback=cc

window.mainloop()
# -----



