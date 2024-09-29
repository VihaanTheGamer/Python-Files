import random
number=random.randint(1,100)
attempts=0

while True:
    try:
        guess=int(input("Guess a number "))
    except:
        print("Invalid value, try again")
        continue

    if guess == number:
        attempts+=1
        print(f" You have guessed the number.The number was {number}")
        print(f" You took {attempts} number of attempts")

        break
    if guess > number:
     print("Guess lower...")
     attempts+=1
     

    if guess < number:
        print("Guess higher...")
        attempts+=1

        


        
