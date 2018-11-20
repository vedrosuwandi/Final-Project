#To Draw the Hour
def hour(pen):
    pen.up()
    pen.goto(0,0)
    pen.setheading(90)
    counter = 12

    for loop in range (0,60):
        #To make the Longer line of the hour
        if loop % 5 == 0:
            pen.up()
            pen.forward(320)
            pen.down()
            pen.color('violet')
            pen.forward(40)
            pen.up()
            pen.backward(70)
            pen.write(counter,font="50")
            if counter == 12:
                counter = 0
            counter += 1

        else:
            # To make the short line of the hour
            pen.up()
            pen.forward(350)
            pen.down()
            pen.forward(10)
            pen.up()
        pen.color("orange")
        pen.goto(0,0)
        pen.right(6)