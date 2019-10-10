from tkinter import *
import tkinter as tk
from tkinter import ttk

root=Tk()
root.geometry("900x500")
root.title("UTS")

label_0=Label(root,text="UTS",width=20,font=15)
label_0.place(x=300,y=10)

label_1=Label(root,text="     NIM",width=20,font=("bold",10),anchor=W)
label_1.place(x=0,y=60)
entry_1=Entry(root)
entry_1.place(x=178,y=100,width=150)

label_2=Label(root,text="     Nama ",width=20,font=("bold",10),anchor=W)
label_2.place(x=0,y=100)
entry_2=Entry(root)
entry_2.place(x=178,y=65,width=250)

label_3=Label(root,text="     Alamat",width=20,font=("bold",10),anchor=W)
label_3.place(x=0,y=140)
entry_3=Entry(root)
entry_3.place(x=178,y=140,width=150)

label_4=Label(root,text="     Jenis Kelamin ",width=20,font=("bold",10),anchor=W)
label_4.place(x=0,y=180)
var=IntVar()
Radiobutton(root,text="Laki-laki",padx=5,variable=var,value=1).place(x=170,y=180)
Radiobutton(root,text="Perempuan",padx=20,variable=var,value=2).place(x=155,y=200)

label_5=Label(root,text="     Baris",width=20,font=("bold",10),anchor=W)
label_5.place(x=500,y=60)
entry_5=Entry(root)
entry_5.place(x=570,y=60,width=50)

win=[]
labelsFrame= ttk.LabelFrame(win)
labelsFrame.place(x=20, y=250)

ttk.Label(labelsFrame, text="NIM").grid(column=0, row=0, padx=30, pady=7)
ttk.Label(labelsFrame, text="Nama").grid(column=1, row=0, padx=70, pady=7)
ttk.Label(labelsFrame, text="Alamat").grid(column=2, row=0, padx=100, pady=7)
ttk.Label(labelsFrame, text="Jenis Kelamin").grid(column=3, row=0, padx=20, pady=7)
def call():
    w= ttk.Label(labelsFrame, text="17041100070").grid(column=0, row=1, padx=30, pady=7)
    x= ttk.Label(labelsFrame, text="Wisnu Sunuadi Desenta").grid(column=1, row=1, padx=70, pady=7)
    y= ttk.Label(labelsFrame, text="Desa Deket Wetan").grid(column=2, row=1, padx=100, pady=7)
    z=ttk.Label(labelsFrame, text="Laki-laki").grid(column=3, row=1, padx=20, pady=7)
    if 
   
Button(root,text="Tambah",width=15,bg="blue",fg="white",command=call).place(x=530,y=180) 

root.mainloop()
