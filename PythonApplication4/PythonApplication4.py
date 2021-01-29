from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import sys, fileinput
from tkinter.messagebox import *

def funktion(a):
    tabs.select(a)

def open_():
    file = askopenfilename()
    for text in fileinput.input(file):
        box.insert(0.0,text)

def save_():
    try:
        file = asksaveasfile(
            mode="w",defaultextension=((".txt"),(".docx")),
            filetypes=(("Notepad",".txt"),("Word",".docx")))
        t=box.get(0.0,END)
        file.write(t)
        file.close()
    except NameError:
        pass

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        main.destroy()
    else:
        showinfo("No")

def imgChange(name,sample):
    global img
    tabs.select(1)
    img=PhotoImage(file=name).subsample(sample)
    can.create_image(10,10,image=img,anchor=NW)

main = Tk()
main.geometry("400x300")
main.title("something")

tabs = ttk.Notebook(main)
text=[1,2,3,4]

tabs1 = Frame(tabs)
tabs2 = Frame(tabs)
tabs3 = Frame(tabs)
tabs4 = Frame(tabs)
tabs.add(tabs1,text=1)
tabs.add(tabs2,text=2)
tabs.add(tabs3,text=3)
tabs.add(tabs4,text=4)
tabs.pack()

M = Menu(main)
main.config(menu=M)
menu = Menu(M,tearoff=0)
M.add_cascade(label="Menu",menu=menu)
menu.add_command(label="Tab1",command=lambda:funktion(0))
menu.add_command(label="Tab2",command=lambda:funktion(1))
menu.add_command(label="Tab3",command=lambda:funktion(2))
menu.add_command(label="Tab4",command=lambda:funktion(3))
menu.add_separator()

smenu = Menu(M,tearoff=1)
M.add_cascade(label="Colors",menu=smenu)
smenu.add_command(label="Color1",command=lambda:main.config(bg="#f9844a"))
smenu.add_command(label="Color2",command=lambda:main.config(bg="#4d908e"))
smenu.add_command(label="Color3",command=lambda:main.config(bg="#f94144"))
smenu.add_command(label="Color4",command=lambda:main.config(bg="#277da1"))
smenu.add_separator()

can=Canvas(tabs2,width=300,height=200)
can.pack()

tmenu = Menu(M,tearoff=1)
M.add_cascade(label="Pictures",menu=tmenu)
tmenu.add_command(label="Dog",command=lambda:imgChange("dog_PNG50348.png",2))
tmenu.add_command(label="Cat",command=lambda:imgChange("cat.png",2))
tmenu.add_command(label="Car",command=lambda:imgChange("car.png",6))
tmenu.add_command(label="Zhigul",command=lambda:imgChange("g.png",3))
tmenu.add_separator()

btn_open = Button(tabs1,text="open",command=open_).grid(row=1,column=0)
btn_save = Button(tabs1,text="save",command=save_).grid(row=1,column=1)
btn_exit = Button(tabs1,text="exit",command=exit_).grid(row=1,column=2)
box = scrolledtext.ScrolledText(tabs1,width=40,height=5).grid(row=0,column=0,columnspan=3)

#img=PhotoImage(file="").subsample(3
#can.create_image(10,10,image=img,anchor=NW)


main.mainloop()