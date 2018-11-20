import time

class Note:
    def __init__(self):
        self.date_v = int(time.strftime("%d"))
        self.month_v = time.strftime("%B")
        self.year_v = int(time.strftime("%Y"))


    def date(self,pen):
        pen.up()
        pen.goto(150,0)
        pen.write(str(self.date_v) + " " + self.month_v + " " + str(self.year_v), font=("Arial", 20, "normal"), align="center")

