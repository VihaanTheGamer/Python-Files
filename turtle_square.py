from turtle import Turtle, Screen

wn = Screen()
vihaan = Turtle()

vihaan.shape("turtle")

for _ in range(4):
    vihaan.forward(100)
    vihaan.left(90)




for _ in range(4):
    vihaan.forward(200)
    vihaan.left(90)
    


for _ in range(4):
    vihaan.forward(300)
    vihaan.left(90)

def square(side_length):
    for _ in range(4):
        vihaan.forward(side_length)
        vihaan.left(90)

square(100)

wn.exitonclick()
    

    
