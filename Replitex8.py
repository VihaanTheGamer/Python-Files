# Import the random module here
import random
# Split string method
while True:
  names_string = input("Give me everybody's names, separated by a comma. ")
  names = names_string.split(", ")
  # 🚨 Don't change the code above 👆
name = random.choice(names)
print(f"{name} is going to buy the meal today!")
  #Write your code below this line 👇
