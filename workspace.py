from tkinter import *

root = Tk()

root['bg'] = '#1e1e1e'
root.title('Умный Конспект')
photo = PhotoImage(file = 'noteicon.png')
root.iconphoto(False, photo)
root.wm_attributes('-alpha', 1)
root.geometry('500x500')
root.resizable(False, False)

f_text= Frame(root)
f_text.pack(fill = BOTH, expand = 1)

text_fild = Text(f_text, 
                    bg='#252526', 
                    fg = 'lightgrey', 
                    padx = 10, 
                    pady = 10,
                    wrap = WORD,
                    insertbackground = 'white',
                    selectbackground = '#d95763',
                    spacing3 = 10,
                    width = 30,
                    )
text_fild.pack(expand = 1, fill = BOTH, side = LEFT)

scroll = Scrollbar(f_text, command = text_fild.yview)
scroll.pack(side = LEFT, fill = Y)
text_fild.config(yscrollcommand = scroll.set)

root.mainloop()