import random
import string
import tkinter as tk
from tkinter import messagebox
parent=tk.Tk()
parent.resizable(width=tk.FALSE,height=tk.FALSE)
parent.geometry("270x80")
parent.title("tk")

def nama () :
    a=string.ascil_letters + string.digits
    return ''.join(random.choice(a)
                   for i in range(panjang))
satu=tk.Label(parent,text='Username',font="Verdana 9").grid(row=0,column=0,sticky='e')
satu1=tk.Entry(parent,width=20,text=nama)
satu1.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=9)

dua=tk.Label(parent,text='Password :',font="Verdana 9").grid(row=1,column=0,stick='e')
dua2=tk.Entry(parent,width=30,show='*',text=nama)
dua2.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=9)

def panggil() :
    box= tk.messagebox.showinfo('info','OK',icon='info')
    if box=='ok':
        parent.destroy()
p=tk.Button(parent,text='Login',font='Times 12',command=panggil)
p.grid(row=2,column=9,stick='e'+'w',padx=2)
