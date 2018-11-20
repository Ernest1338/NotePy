from tkinter import *
from tkinter import filedialog, messagebox

filename="Untitled"

def new():
    global filename
    filename="Untitled"
    t.delete('1.0', END)
    
def openn():
    f = filedialog.askopenfile(mode="r")
    plik = f.read()
    t.delete('1.0', END)
    t.insert(END, plik)
    root.title(f.name+" - Now Editing   | NotePy")

def save():
    global filename
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    tekst = t.get('1.0', END)
    try:
        f.write(tekst)
        root.title(f.name+" - Now Editing   | NotePy")
    except:
        showerror(title="Oops!", message="Unable to save file...")

def about():
    messagebox.showinfo("About", "This program was made by Dawid Janikowski")

root=Tk()

root.title(filename+" - Now Editing   | NotePy")

root.minsize(1280,720)
root.maxsize(1280,720)

t=Text(root, width=1280,height=720)
t.config(font=("courier", 30), fg="black", bg="lightgray")
t.pack()

menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
aboutmenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
menu.add_cascade(label="About", menu=aboutmenu)

filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Open", command=openn)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

aboutmenu.add_command(label="About program", command=about)

root.mainloop()