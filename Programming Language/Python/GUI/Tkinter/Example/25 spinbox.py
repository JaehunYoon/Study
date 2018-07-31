import tkinter

window=tkinter.Tk()
window.title("25 SpinBox")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="숫자를 입력하세요.", height=3)
label.pack()

def value_check(self):
    label.config(text="숫자를 입력하세요.")
    valid = False
    if self.isdigit():
        if (int(self) <= 50 and int(self) >= 0):
            valid = True
    elif self == '':
        valid = True
    return valid

def value_error(self):
    label.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")

validate_command=(window.register(value_check), '%P')
invalid_command=(window.register(value_error), '%P')

spinbox=tkinter.Spinbox(window, from_ = 0, to = 50, validate = 'all', validatecommand = validate_command, invalidcommand=invalid_command)
spinbox.pack()