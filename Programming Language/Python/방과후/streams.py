import tkinter
import tkinter.font
from random import shuffle

# Initialize


# Window Setting
window = tkinter.Tk()

window.title("Streams Board Game")
window.geometry("640x480+100+100")
window.resizable(True, True)

# List Initialize
temp1 = [str(i) for i in range(1, 11)]
temp2 = [str(i) for i in range(11, 21)]
temp3 = [str(i) for i in range(11, 21)]
temp4 = [str(i) for i in range(21, 31)]
temp5 = ['★']
random = temp1 + temp2 + temp3 + temp4 + temp5

shuffle(random)
target = random.pop()
# Temp Label
temp = tkinter.Label(window, text="\t")
temp.grid(row=0, column=0)

# Button
row = 1
column = 1
num = 0
button = list(range(20))


# Grid Setting
for i in range(20):
    button[i] = tkinter.Button(window, text="", overrelief='solid', width=5, height=2, repeatdelay=1000, repeatinterval=100)

for i in range(6):
    button[num].grid(row=row, column=column)
    print(f"row : {row} // column : {column} // num : {num} // i : {i}")
    column += 1
    num += 1

column -= 1
row += 1

for i in range(9):
    button[num].grid(row=row, column=column)
    print(f"row : {row} // column : {column} // num : {num} // i : {i}")
    row += 1
    num += 1
    
row -= 1
column += 1

for i in range(5):
    button[num].grid(row=row, column=column)
    print(f"row : {row} // column : {column} // num : {num} // i : {i}")
    column += 1
    num += 1

# Label
lotto = tkinter.Label(window, text=str(target))
lotto.grid(row=13, column=13, padx=50, pady=20)
# lotto.pack(side="bottom", padx=20, pady=20, anchor='e')

window.mainloop()