from turtle import Turtle, Screen

wn = Screen()
vihaan = Turtle()

vihaan.shape("turtle")
def triangle (side_length):
    for _ in range(3):
        vihaan.forward(side_length)
        vihaan.left(120)

triangle(100)




def triangle (side_length):
    for _ in range(3):
        vihaan.forward(side_length)
        vihaan.left(120)

triangle(200)

wn.exitonclick()

    
