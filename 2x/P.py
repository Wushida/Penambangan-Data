from tkinter import *

root = Tk()

inputstr = StringVar(); outputstr = StringVar()

angka = {'nol': 0, 'satu' : 1, 'dua' : 2, 'tiga' : 3, 'empat' : 4, 'lima' : 5, 'enam' : 6, 'tujuh' : 7, 'delapan' : 8, 'sembilan' : 9, 'sepuluh' : 10, 'sebelas' : 11, 'seratus' : 100}
print(dir(''))
def ubah():
    text = inputstr.get().lower().split(' ')
    n = 0
    total = 0
    for kata in text:
        if kata in angka:
            n = angka[kata]
        if kata == 'belas':
            total += n + 10
            n = 0
        if kata == 'puluh':
            total += n * 10
            n = 0
        if kata == 'ratus':
            total += n * 100
            n = 0
    total += n
    outputstr.set(total)
  
inputstr.trace_add("write", lambda a,b,c: ubah())

Entry (root, textvariable=inputstr).pack()
fm = Frame (root)
fm.pack()
Label(fm, textvariable=outputstr).pack()
root.mainloop()
