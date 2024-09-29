from turtle import Turtle, Screen

scrn = Screen()

vihaan=Turtle()
vihaan.shape("turtle")
scrn.listen()

def go_up():
    vihaan.setheading(90)
    vihaan.forward(50)
def go_down():
    vihaan.setheading(270)
    vihaan.forward(50)
def go_right():
    vihaan.setheading(0)
    vihaan.forward(50)
def go_left():
    vihaan.setheading(180)
def pen_up():
    vihaan.penup()
def pen_down():
    vihaan.pendown()

scrn.onkeypress(go_up, "w")
scrn.onkeypress(go_down, "s")
scrn.onkeypress(go_right, "d")
scrn.onkeypress(go_left, "a")
scrn.onkeypress(pen_up, "Up")
scrn.onkeyrelease(pen_down, "Up")

scrn.exitonclick()  






    
    

    


    

    

    
    
