import tkinter
import ctypes

# --- 해상도 받아오기 ---
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
resolution = f"{screen_width - 100}x{screen_height - 100}"
# ----------------------

window=tkinter.Tk()
window.title("23 bind")
window.geometry(resolution)
window.resizable(True, True)

width=1

def drawing(event):
    if width > 0:
        x1 = event.x - 1
        y1 = event.y - 1
        x2 = event.x + 1
        y2 = event.y + 1
        canvas.create_oval(x1, y1, x2, y2, fill="blue", width=width)

def scroll(event):
    global width
    if event.delta == 120:
        width += 1
    if event.delta == -120:
        width -= 1
    label.config(text=str(width))

canvas=tkinter.Canvas(window, relief="solid", bd=2)
canvas.pack(expand=True, fill="both")
canvas.bind("<B1-Motion>", drawing)
canvas.bind("<MouseWheel>", scroll)

label=tkinter.Label(window, text=str(width))
label.pack()

window.mainloop()