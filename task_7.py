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

arr = []
while True:
    let = input("ВВедите название городов: ")
    arr.append(let.strip())
    if let.strip() == '0':
        break
        
listb = Listbox(root, font="Tahoma 20", widt=20, height=4, selectmode=MULTIPLE)
for a in arr:
    listb.insert(END, a)
    
listb.pack()
root.mainloop()