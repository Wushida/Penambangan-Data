import tkinter as tk
from tkinter import ttk
win=tk.Tk()
label=tk.Label(win, text='Ini ComboBox')
label.grid(column=0, row=0)

#ComboBox
number=tk.StringVar()
ComboBox=ttk.Combobox(win, textvariable=number)
ComboBox.grid(column=0, row=1)
ComboBox['width']= 7
ComboBox['value']=(1,2,3,4,5)


#ComboBox End

win.mainloop()

