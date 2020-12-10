from tkinter import *
import random

def setwindow(root):
    root.title("Window")
    root.resizable(False, False)
    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)
		
    root.geometry("{0}x{1}+{2}+{3}".format(x, h, x, y))

root = Tk()
setwindow(root)

label1 = Label(root, text="Авторизация", font="Tahoma 40")
login = Entry(root, font="Tahoma 15")
password = Entry(root, font="Tahoma 15")
button = Button(root, text="Войти")
label2 = Label(root, text="Логин:", font="Tahoma 15")
label3 = Label(root, text="Пароль:", font="Tahoma 15")

label1.place(relx=0.2, rely=0.2)
login.place(relx=0.35, rely=0.4)
password.place(relx=0.35, rely=0.5)
button.place(relx=0.5, rely=0.6, anchor="center")
label2.place(relx=0.2, rely=0.4)
label3.place(relx=0.2, rely=0.5)

root.mainloop()