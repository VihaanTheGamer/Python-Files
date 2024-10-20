name=input("Enter your name ")
age=int(input("Enter your age "))
salary=float(input("Enter your salary "))
if age<40:
    salary=salary+salary*(5/100)+salary*(10/100)
elif age>=40 and age<=50:
    salary=salary+salary*(7/100)+salary*(12/100)
print("Your total salary is", salary)    
    
    
