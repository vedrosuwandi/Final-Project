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

    Set = ttk.Entry(frame)
    Set.pack()
    Set.insert(2,"example - 15:30:45")

    def submit():
        #To get the value from the input fro
        Timeset = Set.get()
        Current = time.strftime("%H:%M:%S")
        print("the alarm time is: {}".format(Timeset))
        while Timeset != Current:
            Current = time.strftime("%H:%M:%S")
        if Timeset == Current:
            os.system("Alarm.wav")



    button= ttk.Button(frame, text="Set Alarm",command= submit)
    button.pack()



    label2= ttk.Label(frame)
    label2.pack()




