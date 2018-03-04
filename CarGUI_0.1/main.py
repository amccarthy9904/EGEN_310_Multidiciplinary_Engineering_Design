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
	pin_ground = 14
	pin_sleep = 15
        pwmFreq = 100
	
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(pin3, GPIO.OUT)
        GPIO.setup(pin4, GPIO.OUT)
	GPIO.setup(pin_ground, LOW)
	
        pwm1 = GPIO.PWM(pin1, pwmFreq)
        pwm2 = GPIO.PWM(pin2, pwmFreq)
        pwm3 = GPIO.PWM(pin3, pwmFreq)
        pwm4 = GPIO.PWM(pin4, pwmFreq)
        
        self.pwm1.start(0)
        self.pwm2.start(0)
        self.pwm3.start(0)
        self.pwm4.start(0)
        
        self.pauseVar = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master, width=750, height=500)
        f2.grid(row=3, column=3)
        but_pause = Checkbutton(frame, text='Pause', variable=self.pauseVar, command=self.update())
        but_pause.grid(row=0, column=2)
        self.slid_left = Scale(top, from_=100, to=-100, label="LEFT", length=300, tickinterval=20, resolution=2, command=self.update())
        self.slid_right = Scale(top, from_=100, to=-100, label="RIGHT", length=300, tickinterval=20, resolution=2, command=self.update())
        self.slid_left.grid(row=1, column=2)
        self.slid_right.grid(row=1, column=3)

    def update(self):
        if self.pauseVar.get():
            # TODO:
            # pause pi
            boi =1
        else:

            # unpause pi
            # update pi
	if self.slid_left.get() >= 0:
	    self.pwm1.ChangeDutyCycle(self.slid_left.get())
	    self.pwm2.ChangeDutyCycle(0)
	    self.pwm1.start()
	    self.pwm2.start()
	else:
	    self.pwm2.ChangeDutyCycle(abs(self.slid_left.get()))
	    self.pwm1.ChangeDutyCycle(0)
	    self.pwm1.start()
	    self.pwm2.start()



GPIO.setup(pin_sleep, HIGH)
top = Tk()
top.geometry('{}x{}'.format(750, 500))
app = Controller(top)
top.mainloop()
