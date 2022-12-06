import os

from tkinter import *

root = Tk()

def btn_click():
    if name.get() == 'admin':
        if  s_name.get() == 'admin':
            print('Запускаю рабочее пространство...')
            os.system("start cmd /k python workspace.py")
        else:
            print('Не верный пароль или логин.')
    else:
        print('Не верный пароль или логин.')
        
root['bg'] = '#1e1e1e'
root.title('Умный Конспект: Авторизация')
photo = PhotoImage(file = 'noteicon.png')
root.iconphoto(False, photo)
root.wm_attributes('-alpha', 1)
root.geometry('400x500')

root.resizable(False, False)
frame = Frame(root, 
                bg='#252526',
                )
frame.place(x= 60, y = 115)
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
name = Entry(frame)
name.grid(row= 1, column= 1, stick = 'we')
s_name = Entry(frame, show ='*')
s_name.grid(row= 2, column= 1, stick = 'we')
btn = Button(frame, 
                    text = 'Начать',
                    command = btn_click,
                    font = ('Times New Roman', 12, 'normal'),
                    fg = 'white',
                    bg = '#0e639c',
                    )
label_2.grid(row = 1, column = 0, stick = 'we')
label_3.grid(row= 2, column= 0, stick = 'we')
btn.grid(row = 3, column = 0, columnspan= 2, stick = 'we' )
root.mainloop()