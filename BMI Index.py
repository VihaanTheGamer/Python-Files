mass = int(input("Enter your weight "))
height = float(input("Enter your height "))

bmi = mass/(height*height)

print("Yor bmi is:", bmi)

if bmi < 18.5:
    print('Underweight')
if bmi>=18.5 and bmi<25:
    print("Normal")
if bmi >= 25 and bmi < 30:
   print('Overweight')
if bmi >= 30:
   print('Obesity')


