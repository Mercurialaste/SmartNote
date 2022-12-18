import pickle
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

FiLE_NAME = tkinter.NONE

def new_file():
    global FILE_NAME
    FILE_NAME = "Безымянный"
    text.delete('1.0', tkinter.END)
    
def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r", )
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()
    
def save_as():
    out = asksaveasfile(mode='w', defaultextension = 'txt')    
    data = text.get('1.0', tkinter.END)
    try:
            out.write(data.rstrip())
    except Exception:
        showerror(title="Error", message="Ошибка сохранения.")

root = tkinter.Tk()

root['bg'] = '#1e1e1e'
root.title('Умный Конспект')
photo = PhotoImage(file = 'noteicon.png')
root.iconphoto(False, photo)
root.wm_attributes('-alpha', 1)
root.geometry('500x500')
root.resizable(False, False)

f_text= Frame(root)
f_text.pack(fill = BOTH, expand = 1)

text = tkinter.Text(f_text, 
                    bg='#252526', 
                    fg = 'lightgrey', 
                    padx = 10, 
                    pady = 10,
                    wrap = WORD,
                    insertbackground = 'white',
                    selectbackground = '#d95763',
                    spacing3 = 10,
                    width = 30
                    )
text.pack(expand = 1, fill = BOTH, side = LEFT)

scroll = Scrollbar(f_text, command = text.yview)
scroll.pack(side = LEFT, fill = Y)
text.config(yscrollcommand = scroll.set)

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="Создать", command=new_file)
fileMenu.add_command(label="Открыть", command=open_file)
fileMenu.add_command(label="Сохранить", command=save_file)
fileMenu.add_command(label="Сохранить как", command=save_as)
menuBar.add_cascade(label="Файл", menu=fileMenu)
menuBar.add_cascade(label="Выход", command=root.quit)
root.config(menu=menuBar)
root.mainloop()