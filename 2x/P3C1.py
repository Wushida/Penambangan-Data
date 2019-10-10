import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
# demo of side and fill options
tk.Label(frame, text="Pack Demo of side and fill").pack()
tk.Button(frame, text="A").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text="B").pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text="C").pack(side=tk.RIGHT, fill=tk.NONE)
tk.Button(frame, text="D").pack(side=tk.TOP, fill=tk.BOTH)
frame.pack()

#note the top frame does not expand of fill in X or Y directions
#demo of expand options - best uderstood by expanding the root#vwidget ad seeing the effect on all the three buttons below.
tk.Label (root, text="Pack Demo of expand").pack()
tk.Button (root, text="I do not expand").pack()
tk.Button (root, text="I do not fill x but I expand").pack(expand = 1)
tk.Button (root, text="I fill x and expand").pack(fill=tk.X, expand = 1)
root.mainloop()

#RRR
parent = tk.Frame(root)
#placing widget top-down
tk.Button (parent, text="ALL IS WELL").pack(fill=tk.X)
tk.Button (parent, text="BACK TO BASICS").pack(fill=tk.X)
tk.Button (parent, text="CATCH ME IF U CAN").pack(fill=tk.X)
#placing widgets side by side
tk.Button (parent, text="LEFT").pack(side=tk.LEFT)
tk.Button (parent, text="CENTER").pack(side=tk.LEFT)
tk.Button (parent, text="RIGHT").pack(side=tk.LEFT)
parent.pack()
