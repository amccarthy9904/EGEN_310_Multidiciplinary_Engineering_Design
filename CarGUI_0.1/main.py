from tkinter import *
from _thread import *

class Controller:
    def __init__(self, master):
        ## Connection Variables

        self.pauseVar = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master, width=750, height=500)
        f2.grid(row=3, column=3)
        but_pause = Checkbutton(frame, text='Pause', variable=self.pauseVar, command=self.pause)
        but_pause.grid(row=0, column=2)
        slid_left = Scale(top, from_=100, to=-100, label="LEFT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_right = Scale(top, from_=100, to=-100, label="RIGHT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_left.grid(row=1, column=2)
        slid_right.grid(row=1, column=3)

    def pause(self):
        if self.pauseVar.get():
            # TODO:
            # pause pi
            self.update()
        else:
            #self.pause.grid_remove()
            # TODO:
            # unpause pi
            self.update()

    def connect(self, host, port, sock):
        #self.connect.grid(row=3, column=1, sticky=N)
        # TODO:
        # connect to pi
        print('Waiting for a connection')

    def update(self):
        if self.pauseVar.get():
            #self.pause.grid(row=3, column=0, sticky=N)
            # TODO:
            # pause pi
            boi =1
        else:
            #self.pause.grid_remove()
            # TODO:
            # unpause pi
            # update pi
            boi =1


top = Tk()
top.geometry('{}x{}'.format(750, 500))
app = Controller(top)
top.mainloop()
