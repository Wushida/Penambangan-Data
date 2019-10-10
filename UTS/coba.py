from tkinter import Menu
menuBar=Menu(win)
win.config(menu=menuBar)
fileMenu=Menu(menuBar)
fileMenu.add_command(label="New")
menuBar.add_cascade(label="File", menu=fileMenu)
