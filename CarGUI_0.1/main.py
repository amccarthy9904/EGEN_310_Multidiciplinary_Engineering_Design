import Tkinter

class Controller:
    def __init__(self, master):
        self.pauseVar = Tkinter.IntVar()
        frame = Tkinter.Frame(master)
        frame.grid()
        f2 = Tkinter.Frame(master, width=750, height=500)
        f2.grid(row=3, column=2)
        but_pause = Tkinter.Checkbutton(frame, text='Pause', variable=self.pauseVar, command=self.pause)
        but_pause.grid(row=0, column=0)
        but_connect = Tkinter.Button(frame, text='Connect', command=self.connect)
        but_connect.grid(row=0, column=1)
        slid_left = Tkinter.Scale(top, from_=100, to=-100, label="LEFT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_right = Tkinter.Scale(top, from_=100, to=-100, label="RIGHT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_left.grid(row=1, column=0)
        slid_right.grid(row=1, column=1)
        self.pause = Tkinter.Message(f2, text="PAUSE")
        self.connect = Tkinter.Message(f2, text="CONNECT")

    def pause(self):
        if self.pauseVar.get():
            self.pause.grid(row=3, column=0, sticky=Tkinter.N)
            # TODO:
            # pause pi
        else:
            self.pause.grid_remove()
            # TODO:
            # unpause pi
            self.update()

    def connect(self):
        self.connect.grid(row=3, column=1, sticky=Tkinter.N)
        # TODO:
        # connect to pi

    def update(self):
        if self.pauseVar.get():
            self.pause.grid(row=3, column=0, sticky=Tkinter.N)
            # TODO:
            # pause pi
        else:
            self.pause()
            # TODO:
            # unpause pi
            # update pi


top = Tkinter.Tk()
top.geometry('{}x{}'.format(750, 500))
app = Controller(top)
top.mainloop()
