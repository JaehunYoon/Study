import requests
import tkinter
from urllib.parse import quote
from bs4 import BeautifulSoup

user = {}

window = tkinter.Tk()

window.title("OP.GG")
window.geometry("1280x1080")
window.resizable(True, True)

image = tkinter.PhotoImage(file="../Project/main.PNG")
title_image = tkinter.Label(window, image=image)
title_image.pack()

def summoner_name(event):
    user['summoner_name'] = f'{input_username.get()}'

    if summoner_name == []:
        label.config(text="OP.GG에 등록되지 않은 소환사입니다. 오타를 확인 후 다시 검색해주세요.")
    else:
        label.config(text=f"소환사명 : {user['summoner_name']}")
    

input_username = tkinter.Entry(window)
input_username.bind("<Return>", summoner_name)
input_username.pack()

label = tkinter.Label(window)
label.pack()


window.mainloop()