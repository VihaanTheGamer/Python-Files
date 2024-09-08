from turtle import Turtle, Screen

wn = Screen()
vihaan = Turtle()

vihaan.shape("turtle")


def drawpoly(sides,side_length):
    angle=360/sides
    for i in range(sides):

        vihaan.forward(side_length)
        vihaan.left(angle)

a=int(input("Enter a number"))
drawpoly(a, 100)    
        

def square(side_length):
    for i in range(4):
        angle=360/4
        vihaan.forward(side_length)
        vihaan.left(angle)

#square(100)        
        
        
        
    




wn.exitonclick()




