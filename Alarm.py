import time
from tkinter import *

import os



def alarm():
    #To make the alarm window
    root = Tk()
    root.title("Alarm")
    # ttk is to give access to the
    frame= Frame(root)
    frame.pack()


    label1 = Label(frame,text="Alarm")
    label1.pack()

    Set = Entry(frame)
    Set.pack()
    Set.insert(2,"example - 15:30:45")

    def submit():
        #To get the value from the input from the Set
        Timeset = Set.get()
        Current = time.strftime("%H:%M:%S")
        print("the alarm time is: {}".format(Timeset))
        while Timeset != Current:
            Current = time.strftime("%H:%M:%S")
        if Timeset == Current:
            os.system("Alarm.wav")



    button = Button(frame, text="Set Alarm",command= submit)
    button.pack()



    




