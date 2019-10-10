from tkinter import *

root=Tk()
root.geometry("600x200")
root.title("Konversi Huruf ke Angka")

label_0=Label(root,text="Konversi Huruf ke Angka",width=20,font=15)
label_0.place(x=200,y=10)

label_1=Label(root,text="     Terbilang ",width=20,font=("bold",10),anchor=W)
label_1.place(x=0,y=60)
entry_1=Entry(root)
entry_1.place(x=178,y=65,width=250)

def konversi(x):
    angka = {'nol': 0, 'satu' : 1, 'dua' : 2,
            'tiga' : 3, 'empat' : 4, 'lima' : 5,
            'enam' : 6, 'tujuh' : 7, 'delapan' : 8,
            'sembilan' : 9, 'sepuluh' : 10, 'sebelas' : 11,
            'seratus' : 100}
    def x():
        text=entry_1.get(
        n=0
        total = 0
        for kata in text:
            if kata in angka:
                n = angka[kata]
            if kata == 'puluh':
                total += n * 10
                n = 0
            if kata == 'ratus':
                total += n * 100
                n = 0
        total += n
        
        return total

def call():
    root2=Toplevel(root)
    root2.geometry("600x100")
    text=entry_1.get()
    ww=str(text)
    wx=int(konversi(ww))
    a=Label(root2,text="Konversi Huruf ke Angka",width=20,font=15)
    a.place(x=200,y=3)
    label_1=Label(root2,text="     Angka : ",width=20,font=("bold",10),anchor=W)
    label_1.place(x=0,y=40)
    Tmpl_1=Label(root2,text=wx,fg="black")
    Tmpl_1.place(x=178,y=45)
    
Button(root,text="Finish",width=15,bg="black",fg="white",command=call).place(x=450,y=150) 

root.mainloop()
