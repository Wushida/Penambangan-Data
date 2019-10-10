import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
win.resizable(0,0)

ttk.Label(win, text="A Label").grid(column=0, row=0)

aLabel= ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)
def clickMe():
    action.configure(text="** I have been Clicked! **")
    aLabel.configure(foreground='red')

    action.configure(text="Hello " + name.get())

#Adding a Button
action=ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)

#Modifed Button
action.grid(column=1, row=1)

ttk.Label(win, text="Enter a name").grid(column=0, row=0)

name=tk.StringVar()
nameEntered=ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

win.mainloop()
