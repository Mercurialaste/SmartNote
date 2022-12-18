import os, pickle
from tkinter import *
from tkinter import messagebox


root = Tk()
def registration():
    text = Label(frame, 
                text="Регистрация",
                font = ('Times New Roman', 12, 'normal'),
                fg = 'white',
                bg = '#252526'
                )
    text.grid(row = 0, column= 1, stick= 'we')
    label_2 = Label(frame,
                    text = 'Имя пользователя:',
                    anchor = 'w',
                    fg = 'lightgrey', 
                    bg = '#252526',
                    font = ('Times New Roman', 14, 'normal'),
                    )
    label_2.grid(row = 1, column = 0, stick = 'we')
    registr_login = Entry(frame)
    registr_login.grid(row= 1, column= 1, stick= 'we')
    label_3 = Label(frame,
                    text = 'Пароль:',
                    anchor = 'w',
                     fg = 'lightgrey', 
                    bg = '#252526',
                    font = ('Times New Roman', 14, 'normal'),
                    )
    registr_pass = Entry(frame, show ='*')
    registr_pass.grid(row= 2, column= 1, stick = 'we')
    button_registr = Button(frame, 
                            text="Зарегестрироватся", 
                            command = lambda: save(),
                            font = ('Times New Roman', 12, 'normal'),
                            fg = 'white',
                            bg = '#0e639c'
                            )
    button_registr.grid(row=3, column=1, stick='we')
    label_3.grid(row= 2, column= 0, stick = 'we')
    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_pass.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()

def login():
    text = Label(frame, 
                text="Вход",
                font = ('Times New Roman', 12, 'normal'),
                fg = 'white',
                bg = '#252526'
                )
    text.grid(row = 0, column= 1, stick= 'we')
    label_2 = Label(frame,
                    text = 'Имя пользователя:',
                    anchor = 'w',
                    fg = 'lightgrey', 
                    bg = '#252526',
                    font = ('Times New Roman', 14, 'normal'),
                    )
    enter_login = Entry(frame)
    enter_login.grid(row= 1, column= 1, stick = 'we')
    label_2.grid(row = 1, column = 0, stick = 'we')
    label_3 = Label(frame,
                    text = 'Пароль:',
                    anchor = 'w',
                     fg = 'lightgrey', 
                    bg = '#252526',
                    font = ('Times New Roman', 14, 'normal'),
                    )
    label_3.grid(row= 2, column= 0, stick = 'we')
    enter_pass = Entry(frame, show ='*')
    enter_pass.grid(row= 2, column= 1, stick = 'we')
    button_login = Button(frame, 
                            text="Вход", 
                            command = lambda: log_pass(),
                            font = ('Times New Roman', 12, 'normal'),
                            fg = 'white',
                            bg = '#0e639c'
                            )
    button_login.grid(row=3, column=1, stick= 'we')

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                print('Запускаю рабочее пространство...')
                os.system("start cmd /k python workspace.py")
            else: 
                messagebox.showerror("Ошибка", "Не верный логин или пароль.")
        else:
             messagebox.showerror("Ошибка", "Не верный логин или пароль.")



        
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
frame.place(x= 60, y = 165)
btn = Button(frame, 
                    text = 'Авторизация',
                    command = lambda: login(),
                    font = ('Times New Roman', 12, 'normal'),
                    fg = 'white',
                    bg = '#0e639c',
                    )
btn_2 = Button(frame, 
                    text = 'Зарегестрироватся',
                    command = lambda: registration(),
                    font = ('Times New Roman', 12, 'normal'),
                    fg = 'white',
                    bg = '#0e639c',
                    )
btn.grid(row = 3, column = 0, columnspan= 1, stick = 'we' )
btn_2.grid(row = 4, column = 0, columnspan = 1, stick = 'we')

root.mainloop()