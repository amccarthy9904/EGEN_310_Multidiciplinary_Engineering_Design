from tkinter import *
import socket
import sys
from _thread import *

class Controller:
    def __init__(self, master):
        ## Connection Variables
        host = 'localhost'
        port = 8888
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.pauseVar = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master, width=750, height=500)
        f2.grid(row=3, column=3)
        but_pause = Checkbutton(frame, text='Pause', variable=self.pauseVar, command=self.pause)
        but_pause.grid(row=0, column=2)
        but_connect = Button(frame, text='Connect', command=self.connect(host, port, sock))
        but_connect.grid(row=0, column=1)
        slid_left = Scale(top, from_=100, to=-100, label="LEFT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_right = Scale(top, from_=100, to=-100, label="RIGHT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_left.grid(row=1, column=2)
        slid_right.grid(row=1, column=3)
        #self.pause = Message(f2, text="PAUSE")
        #self.connect = Message(f2, text="CONNECT")

    def pause(self):
        if self.pauseVar.get():
            self.update()
            #self.pause.grid(row=3, column=0, sticky=N)
            # TODO:
            # pause pi
        else:
            #self.pause.grid_remove()
            # TODO:
            # unpause pi
            self.update()

    def connect(self, host, port, sock):
        #self.connect.grid(row=3, column=1, sticky=N)
        # TODO:
        # connect to pi
        try:
            sock.bind((host, port))
        except socket.error as err:
            print(str(err))
        sock.listen(5)
        print('Waiting for a connection')
        #conn, addr = sock.accept()
        #start_new_thread(self.client_thread(), (conn,))

    def client_thread(self, conn):
        conn.send(str.encode('welcome~~~~~\n'))
        while True:
            data = conn.recv(2048)
            reply = 'Server output:\t' + data.decode('utf-3')
            if not data:
                break
            conn.sendall(str.encode(reply))


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
