from View import *
from Alarm import *
from Timer import *



class Apps:
    def __init__(self,frame):
        #To organize the app
        self.View = Button(frame, text="View Clock",command=view,height=10,width=50)
        self.View.pack()
        self.Alarm = Button(frame,text = "Alarm",command=alarm,height=10,width=50)
        self.Alarm.pack()
        self.Timer = Button(frame,text="Timer",command=timer,height=10,width=50)
        self.Timer.pack()
        self.Quit = Button(frame,text="Quit",command=cancel,height=10,width=50)
        self.Quit.pack()


def cancel():
    wn.destroy()

wn = Tk()
wn.title("Time Application")
frame = Frame(wn)
frame.pack()
Apps(wn)
wn.mainloop()

