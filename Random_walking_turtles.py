import random
from turtle import Turtle, Screen

scrn = Screen()
scrn.setup(600, 600)
scrn.bgcolor("black")

colors = ["cyan","yellow","red","orange"]


all_turtles = []
for i in range(4):
    cyan = Turtle()
    cyan.shape("turtle")
    cyan.color(colors[i])
    all_turtles.append(cyan)
    
while True:
    for cyan in all_turtles:
        
        random_move = random.randint(10, 100)
        random_turn = random.randint(0, 360)

        if cyan.xcor() > 280:
            cyan.setheading(180)
            cyan.forward(100)

        if cyan.ycor() > 280:
            cyan.setheading(270)
            cyan.forward(100)

        if cyan.xcor() < -280:
             cyan.setheading(0)
             cyan.forward(100)

        if cyan.ycor() < -280:
             cyan.setheading(90)
             cyan.forward(100)

        cyan.setheading(random_turn)
        cyan.forward(random_move)

        

