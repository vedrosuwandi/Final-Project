from tkinter import *
import time
import os

def timer():
    #The timer feature
    wn2 = Tk()
    wn2.title("Timer")
    frame = Frame(wn2)
    frame.pack()
    label = Label(frame,text="Timer")
    label.pack()
    entry = Entry(frame,width = 10)
    entry.pack()
    entry.insert(3,"Number")
    def count():
        #To get the input to the timer
        seconds = int(entry.get())
        while seconds >= 1:
            seconds -= 1
            print(seconds + 1)
            time.sleep(1)
        if seconds == 0 :
            os.system("Time_Up.wav")
            label2 = Label(frame,text="Time's up")
            label2.pack()
    button = Button(frame,text="Start",command = count)
    button.pack()


