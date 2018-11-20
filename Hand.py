from Clock_face import centre
import time

#Make the hour hand
def Hour_hand(pen):
    hour = int(time.strftime("%I"))
    centre(pen)
    pen.setheading(90)
    pen.pensize(10)
    pen.color("green")
    #1 hour = 30 degree
    hour_angle = (hour / 12) * 360
    pen.right(hour_angle)
    pen.down()
    # To make how long the hand
    pen.forward(150)

#Make the minute hand
def Min_hand(pen):
    mins = int(time.strftime("%M"))
    centre(pen)
    pen.setheading(90)
    pen.color("blue")
    pen.up()
    mins_angle = (mins / 60) * 360
    pen.right(mins_angle)
    pen.down()
    pen.pensize(10)
    pen.forward(250)

#Make the second hand
def Sec_hand(pen):
    sec = int(time.strftime("%S"))
    pen.home()
    pen.setheading(90)
    pen.color("red")
    pen.down()
    pen.pensize(5)
    sec_angle = ((sec/60) * 360) + 6
    pen.right(sec_angle)
    pen.forward (300)
