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

text = Text(root, bd=2, font="Tahoma 20", widt=30)
handler = open(Файл, 'r')
text_file = handler.read()
text.insert(END, text_file)
handler.close()

scroll = Scrollbar(root, command=text.yview, orient=VERTICAL)
text['yscrollcommand'] = scroll.set

text.pack(side="left")
scroll.pack(side="left", fill=Y)

root.mainloop()