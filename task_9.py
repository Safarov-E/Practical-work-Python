from tkinter import *
from cmath import *

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

def handlerDiscriminant(event):
    a = int(text1.get())
    b = int(text2.get())
    c = int(text3.get())

    discrimamt = (b**2)-(4*a*c)
    x1 = ((-b) + sqrt(discrimamt)) / (a * 2)
    x2 = ((-b) - sqrt(discrimamt)) / (a * 2)

    if discrimamt > 0:
        labelx1['text'] = x1
        labelx2['text'] = x2
    elif discrimamt < 0:
        labelx1['text'] = 'Нет корней'
    else:
        labelx1['text'] = x1
        labelx2['text'] = 'Нет корней'


label = Label(root, text="ax^2 + bx + c = 0", font="Tahoma 20")
labela = Label(root, text="a:", font="Tahoma 20")
labelb = Label(root, text="b:", font="Tahoma 20")
labelc = Label(root, text="c:", font="Tahoma 20")
text1 = Entry(root, font="Tahoma 20")
text2 = Entry(root, font="Tahoma 20")
text3 = Entry(root, font="Tahoma 20")
button = Button(root, text="Вычислить корни уравнения", font="Tahoma 20")
labelx1 = Label(root, font="Tahoma 20")
labelx2 = Label(root, font="Tahoma 20")

label.pack()
text1.place(relx=0.3, rely=0.1)
text2.place(relx=0.3, rely=0.2)
text3.place(relx=0.3, rely=0.3)
labela.place(relx=0.2, rely=0.1)
labelb.place(relx=0.2, rely=0.2)
labelc.place(relx=0.2, rely=0.3)
button.place(relx=0.2, rely=0.4)
labelx1.place(relx=0.2, rely=0.5)
labelx2.place(relx=0.4, rely=0.5)

button.bind("<Button-1>", handlerDiscriminant)

root.mainloop()