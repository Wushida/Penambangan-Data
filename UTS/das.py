from tkinter import *

class MembuatKolomTeks(Frame) :
    def __init__(self) :
        self.buatTeks()
        self.buatKolom()
        self.buatTombol()

    def buatTeks(self):
        Label(text="First Name").grid(row=0)
        Label(text="Last Name").grid(row=1)

    def buatKolom(self):
        self.kolom1 = Entry()
        self.kolom2 = Entry()

        self.kolom1.insert(10, "masukkan nama disini")
        self.kolom2.insert(10, "nama akhirnya disini")

        self.kolom1.grid(row=0, column=1)
        self.kolom2.grid(row=1, column=1)

    def buatTombol(self):
       Button(text='Show', command=self.perintah).grid(row=3, column=1)

    def perintah(self):
        print("First Name: %s \nLast Name: %s" % (self.kolom1.get(), self.kolom2.get()))

master = Tk()
MembuatKolomTeks()
mainloop()
