import os

from tkinter import *

root = Tk()

def btn_click():
    print('''Работает...
Запускаю рабочее пространство...''')
    os.system("start cmd /k python workspace.py")   
root['bg'] = '#1e1e1e'
root.title('Умный Конспект')
photo = PhotoImage(file = 'noteicon.png')
root.iconphoto(False, photo)
root.wm_attributes('-alpha', 1)
root.geometry('500x700')

root.resizable(False, False)
frame = Frame(root, 
                bg='#252526',
                )
frame.pack()

lable_1 = Label(frame, 
                text = '''Приветствуем в приложении 
"Умный Конспект"''',
                anchor = 'n',
                font = ('Times New Roman', 14, 'normal'),
                fg = 'lightgrey', 
                bg = '#252526',
                width = 30,
                height = 2, 
                )
label_2 = Label(frame,
                    text = 'Имя пользователя:',
                    anchor = 'w',
                    fg = 'lightgrey', 
                    bg = '#252526',
                    font = ('Times New Roman', 14, 'normal'),
                    )
label_3 = Label(frame,
                    text = 'Пароль:',
                    anchor = 'w',
                     fg = 'lightgrey', 
                    bg = '#252526',
                    font = ('Times New Roman', 14, 'normal'),
                    )
btn = Button(root, 
                    text = 'Начать',
                    command = btn_click,
                    font = ('Times New Roman', 12, 'normal'),
                    fg = 'white',
                    bg = '#0e639c',
                    )
lable_1.pack()
label_2.pack()
label_3.pack()
btn.place(x = 180, y = 460, width = 150, height = 40)

root.mainloop()