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
    satuan = [' ', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    hasil = 0
        
    if x == satuan[1] :
        hasil += 1
    elif x == satuan[2] :
        hasil += 2
    elif x == satuan[3] :
        hasil += 3
    elif x == satuan[4] :
        hasil += 4
    elif x == satuan[5] :
        hasil += 5
    elif x == satuan[6] :
        hasil += 6
    elif x == satuan[7] :
        hasil += 7
    elif x == satuan[8] :
        hasil += 8
    elif x == satuan[9] :
        hasil += 9
    elif x == satuan[10] :
        hasil += 10
    elif x == satuan[11] :
        hasil += 11
    elif x == satuan[2] + ' belas':
        hasil += 12
    elif x == satuan[3] + ' belas':
        hasil += 13
    elif x == satuan[4] + ' belas':
        hasil += 14
    elif x == satuan[5] + ' belas':
        hasil += 15
    elif x == satuan[6] + ' belas':
        hasil += 16
    elif x == satuan[7] + ' belas':
        hasil += 17
    elif x == satuan[8] + ' belas':
        hasil += 18
    elif x == satuan[9] + ' belas':
        hasil += 19
    
    return hasil

def call():
    root2=Toplevel(root)
    root2.geometry("600x100")
    show_1=entry_1.get()
    ww=str(show_1)
    wx=int(konversi(ww))
    a=Label(root2,text="Konversi Huruf ke Angka",width=20,font=15)
    a.place(x=200,y=3)
    label_1=Label(root2,text="     Angka : ",width=20,font=("bold",10),anchor=W)
    label_1.place(x=0,y=40)
    Tmpl_1=Label(root2,text=wx,fg="black")
    Tmpl_1.place(x=178,y=45)
    
Button(root,text="Finish",width=15,bg="black",fg="white",command=call).place(x=450,y=150) 

root.mainloop()
