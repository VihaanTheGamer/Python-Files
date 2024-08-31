print("Please select a shape for which you would like to take out perimeter.")
print("square")
print("rectangle")
shape=input(":")
print("Shape is", shape)
if shape=="square":
  side=int(input("Please tell a side in m: "))
  perimeter=(side*4)
  print("Perimeter of square is -  ",perimeter)

if shape=="rectangle":
       Length=int(input("Please provide a length of rectangle in m:  "))
       Breadth=int(input("Please provide a breadth of rectangle in m:  "))
       Perimeter=2*(Length+Breadth)
       print("Perimeter of rectangle is - ",Perimeter)
   
