import time
from tkinter import *
import tkinter as ttk
import os



def alarm():
    #To make the alarm window
    root = Tk()
    root.title("Alarm")
    frame= ttk.Frame(root)
    frame.pack()


    label1 = ttk.Label(frame,text="Alarm")
    label1.pack()

    entry1 = ttk.Entry(frame)
    entry1.pack()
    entry1.insert(2,"example - 15:30:45")

    def submit():
        #To get the value from the input from entry
        Timeset = entry1.get()
        Current = time.strftime("%H:%M:%S")
        print("the alarm time is: {}".format(Timeset))
        while Timeset != Current:
            Current = time.strftime("%H:%M:%S")
        if Timeset == Current:
            os.system("Alarm.wav")



    button1= ttk.Button(frame, text="Set Alarm",command= submit)
    button1.pack()



    label2= ttk.Label(frame)
    label2.pack()




