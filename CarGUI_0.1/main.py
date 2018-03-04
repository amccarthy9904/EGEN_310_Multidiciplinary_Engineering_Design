from tkinter import *
from _thread import *
import RPi.GPIO as GPIO

class Controller:
    def __init__(self, master):

        GPIO.setmode(GPIO.BOARD)
        pin1 = 10
        pin2 = 11
        pin3 = 12
        pin4 = 13

        pwmFreq = 100

        GPIO.setup(pin1, GPIO.out)
        GPIO.setup(pin2, GPIO.out)
        GPIO.setup(pin3, GPIO.out)
        GPIO.setup(pin4, GPIO.out)

        pwm1 = GPIO.PWM(pin, pwmFreq)
        pwm2 = GPIO.PWM(pin, pwmFreq)
        pwm3 = GPIO.PWM(pin, pwmFreq)
        pwm4 = GPIO.PWM(pin, pwmFreq)
        
        pwm1.start(0)
        pwm2.start(0)
        pwm3.start(0)
        pwm4.start(0)
        
        self.pauseVar = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master, width=750, height=500)
        f2.grid(row=3, column=3)
        but_pause = Checkbutton(frame, text='Pause', variable=self.pauseVar, command=self.update())
        but_pause.grid(row=0, column=2)
        slid_left = Scale(top, from_=100, to=-100, label="LEFT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_right = Scale(top, from_=100, to=-100, label="RIGHT", length=300, tickinterval=20, resolution=2, command=self.update())
        slid_left.grid(row=1, column=2)
        slid_right.grid(row=1, column=3)

    def update(self):
        if self.pauseVar.get():
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
