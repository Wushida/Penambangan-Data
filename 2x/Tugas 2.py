from tkinter import *

root=Tk()
root.geometry("600x600")
root.title("Data diri mahasiswa")

label_0=Label(root,text="DATA DIRI MAHASISWA",width=20,font=15)
label_0.place(x=200,y=10)

label_1=Label(root,text="     Nama ",width=20,font=("bold",10),anchor=W)
label_1.place(x=0,y=60)
entry_1=Entry(root)
entry_1.place(x=178,y=65,width=250)

label_2=Label(root,text="     NIM",width=20,font=("bold",10),anchor=W)
label_2.place(x=0,y=100)
entry_2=Entry(root)
entry_2.place(x=178,y=100,width=150)

label_3=Label(root,text="     Jurusan",width=20,font=("bold",10),anchor=W)
label_3.place(x=0,y=140)
entry_3=Entry(root)
entry_3.place(x=178,y=140,width=150)

label_4=Label(root,text="     Tanggal Lahir ",width=20,font=("bold",10),anchor=W)
label_4.place(x=0,y=180)
entry_4=Entry(root)
entry_4.place(x=178,y=180,width=150)

label_5=Label(root,text="     Jenis Kelamin ",width=20,font=("bold",10),anchor=W)
label_5.place(x=0,y=220)
var=IntVar()
Radiobutton(root,text="Laki-laki",padx=5,variable=var,value=1).place(x=170,y=220)
Radiobutton(root,text="Perempuan",padx=20,variable=var,value=2).place(x=155,y=240)

label_6=Label(root,text="     Agama",width=20,font=("bold",10),anchor=W)
label_6.place(x=0,y=280)
v=IntVar()
Radiobutton(root,text="Islam",padx=5,variable=v,value=1).place(x=170,y=280)
Radiobutton(root,text="Hindu",padx=20,variable=v,value=2).place(x=155,y=300)
Radiobutton(root,text="Budha",padx=5,variable=v,value=3).place(x=170,y=320)
Radiobutton(root,text="Khatolik",padx=20,variable=v,value=4).place(x=240,y=280)
Radiobutton(root,text="Kristen Protestan",padx=5,variable=v,value=5).place(x=255,y=300)
Radiobutton(root,text="Kong Hu Cu",padx=20,variable=v,value=6).place(x=240,y=320)

label_7=Label(root,text="     Alamat",width=20,font=("bold",10),anchor=W)
label_7.place(x=0,y=360)
entry_7=Entry(root)
entry_7.place(x=178,y=360,width=250)

label_8=Label(root,text="     No.Telpon",width=20,font=("bold",10),anchor=W)
label_8.place(x=0,y=400)
entry_8=Entry(root)
entry_8.place(x=178,y=400,width=150)


def call():
    root2=Toplevel(root)
    root2.geometry("600x700")
    show_1=entry_1.get()
    show_2=entry_2.get()
    show_3=entry_3.get()
    show_4=entry_4.get()
    show_5=var.get()
    show_6=v.get()
    show_7=entry_7.get()
    show_8=entry_8.get()
    a=Label(root2,text="DATA DIRI MAHASISWA",width=20,font=15)
    a.place(x=200,y=3)
    label_1=Label(root2,text="     Nama",width=20,font=("bold",10),anchor=W)
    label_2=Label(root2,text="     NIM",width=20,font=("bold",10),anchor=W)
    label_3=Label(root2,text="     Jurusan",width=20,font=("bold",10),anchor=W)
    label_4=Label(root2,text="     Tanggal Lahir ",width=20,font=("bold",10),anchor=W)
    label_5=Label(root2,text="     Jenis Kelamin ",width=20,font=("bold",10),anchor=W)
    label_6=Label(root2,text="     Agama",width=20,font=("bold",10),anchor=W)
    label_7=Label(root2,text="     Alamat",width=20,font=("bold",10),anchor=W)
    label_8=Label(root2,text="     No.Telpon",width=20,font=("bold",10),anchor=W)
    label_1.place(x=0,y=40)
    label_2.place(x=0,y=80)
    label_3.place(x=0,y=120)
    label_4.place(x=0,y=160)
    label_5.place(x=0,y=200)
    label_6.place(x=0,y=240)
    label_7.place(x=0,y=280)
    label_8.place(x=0,y=320)
    Tmpl_1=Label(root2,text=show_1,fg="black")
    Tmpl_2=Label(root2,text=show_2,fg="black")
    Tmpl_3=Label(root2,text=show_3,fg="black")
    Tmpl_4=Label(root2,text=show_4,fg="black")
    Tmpl_5=Label(root2,text=show_5,fg="black")
    Tmpl_6=Label(root2,text=show_6,fg="black")
    Tmpl_7=Label(root2,text=show_7,fg="black")
    Tmpl_8=Label(root2,text=show_8,fg="black")
    Tmpl_1.place(x=178,y=45)
    Tmpl_2.place(x=178,y=80)
    Tmpl_3.place(x=178,y=120)
    Tmpl_4.place(x=178,y=160)
    Tmpl_5.place(x=178,y=202)
    Tmpl_6.place(x=178,y=240)
    Tmpl_7.place(x=178,y=280)
    Tmpl_8.place(x=178,y=320)
    
Button(root,text="Finish",width=15,bg="blue",fg="white",command=call).place(x=450,y=450) 

root.mainloop()
