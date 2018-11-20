#To draw a clock face
def draw(pen):
    #To make the line disappear
    pen.up()
    #To make the position of the circle
    pen.goto(0,360)
    #To make the direction (Quadrant)
    pen.setheading(180)
    pen.down()
    pen.color("black")
    pen.pensize(15)
    #To set the radius
    pen.circle(360)

# make the center
def centre(pen):
    pen.down()
    pen.goto(0, 0)