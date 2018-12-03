import requests
import tkinter
import tkinter.ttk
import webbrowser
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
# window.state("zoomed") -> Full Screen
window.resizable(True, True)

# Menu
menubar = tkinter.Menu(window)
menu = tkinter.Menu(menubar, tearoff=0)
menu.add_command(label="Github : https://github.com/JaehunYoon")
menu.add_command(label="Email : goodasd123@naver.com")
menu.add_separator()
menu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label="메뉴", menu=menu)
window.config(menu=menubar)

champ_temp = []
kda_champ_temp = []
summoner = ""

# Frame, ScrollBar
frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side='right', fill="y")

# Main title Image
image = tkinter.PhotoImage(file="main.PNG")
title_image = tkinter.Label(window, image=image)
title_image.pack()


def summoner_name(event):
    champion_list = []
    winrate_list = []
    kda_list = []
    kda_average_list = []
    global champ_temp
    global kda_champ_temp
    global summoner
    
    most_champion_list.delete(0, 'end')
    user = get_username(input_username.get())
    summoner = user['summoner_name']

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
            champion_list.append(champion['data-value'])
        
        # Champion Win Rate
        for champ in get_most_champion(input_username.get()):
            champion_list.append(champ['data-value'])

        for win in get_champion_winrate(input_username.get()):
            winrate_list.append(win.text)

        # Champion KDA
        for kda in get_champion_kda(input_username.get()):
            kda_list.append(rm_escape_sequence(kda.text))
        
        for avg in get_kda_average(input_username.get()):
            kda_average_list.append(avg['data-value'])

        champ_temp = list(zip(champion_list, winrate_list))
        kda_champ_temp = list(zip(kda_list, kda_average_list))
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

# TreeView
def champion_winrate():
    global champ_temp
    kda_tell = ""
    winrate_tell = ""

    subtree_value = 4
    # def cc(self):
    #     treeview.tag_configure("selected", background="red")
    
    sub_screen = tkinter.Toplevel(window)
    sub_screen.geometry("640x480+700+100")
    treeview = tkinter.ttk.Treeview(sub_screen, columns=["one", "two"])
    treeview.pack()

    treeview.column("#0", width=200)
    treeview.heading("#0", text="Most", anchor="center")

    treeview.column("one", width=150, anchor="center")
    treeview.heading("one", text="챔피언", anchor="center")

    treeview.column("#2", width=200, anchor="center")
    treeview.heading("two", text="승률", anchor="center")

    treelist = champ_temp
    top = list(range(len(treelist)))
    top_mid = [[0 for _ in range(subtree_value)] for _ in range(len(treelist))]

    for i in range(len(treelist)):
        top[i] = treeview.insert('', 'end', text=i+1, values=treelist[i], tags="tag1")
        # Test - User | KDA | Winrate
        user_win_rate = float(treelist[i][1].replace('%', ''))
        average = get_champion_average_winrate(remove_special_char(treelist[i][0]))
        average_win_rate = ""
        if average == "고인이여서 확인이 불가능합니다.":
            average_win_rate = average
            winrate_tell = "고인"
        else:
            average_win_rate = float(average.replace('%', ''))
        
            if user_win_rate > average_win_rate:
                winrate_tell = "평균보다 승률이 높습니다!"
            elif user_win_rate < average_win_rate:
                winrate_tell = "남들보다 못하네요.."
            elif user_win_rate == average_win_rate:
                winrate_tell = "딱 평균 실력이네요."
            
            average_win_rate = str(average_win_rate) + '%'

        top_mid[i][0] = treeview.insert(top[i], 'end', text="User", values=["KDA", "승률"])
        top_mid[i][1] = treeview.insert(top[i], 'end', text=f"{summoner}", values=[f"{kda_champ_temp[i][0]} ({kda_champ_temp[i][1]})", f"{treelist[i][1]}"])
        top_mid[i][2] = treeview.insert(top[i], 'end', text="평균", values=["준비중입니다", f"{average_win_rate}"])
        top_mid[i][3] = treeview.insert(top[i], 'end', text="=>", values=["준비중입니다", winrate_tell])

    treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>") # , callback=cc

window.mainloop()
# -----

'''
* To do
- top_mid에 평균 리스트 뽑아오기
- op.gg 통계 사이트의 html 소스가 안 뽑아진다.!!!!
'''