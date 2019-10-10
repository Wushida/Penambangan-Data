from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.geometry('460x200')
root.title('Angka Terbilang')

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

def konversia():
    a = kolom.get()
    b = str(a)
    c = int(konversi(b))

    

kolom = Entry(root, width=70)
kolom.grid(row=0, column=0, padx=3)

tombol = Button(root, text='Go', bg='black', fg='green', command=konversia)
tombol.grid(row=0, column=1, sticky=W)

label= Text(root, width=50, height=10)
label.grid(row=1, columnspan=2, pady=3)

root.mainloop()
