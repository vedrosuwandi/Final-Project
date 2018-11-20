import time
import turtle
import Hour
import Clock_face
import Hand
from Note import Note



def digital(pen):
    pen.up()
    pen.goto(0,150)
    current_time = time.strftime("%H:%M:%S")
    pen.write(current_time, font=("Arial", 20, "normal"), align="center")

note = Note()




def view():
    # To set the turtle module
    clock = turtle.Screen()
    clock.bgcolor("white")
    clock.setup(width=770, height=770)
    clock.title("Clock")
    clock.tracer(0)
    # Create the drawing pen
    pen = turtle.Turtle()
    # To hide the pen
    pen.hideturtle()


    while True:
        Clock_face.draw(pen)
        Hour.hour(pen)
        note.date(pen)
        digital(pen)
        Hand.Min_hand(pen)
        pen.clear()
        Hand.Hour_hand(pen)
        Hand.Sec_hand(pen)

        time.sleep(1)