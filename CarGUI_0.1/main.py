from tkinter import *

top = Tk()
left = Scale(top, from_=-100, to=100)
right = Scale(top, from_=-100, to=100)
right.pack()
left.pack()
top.mainloop()