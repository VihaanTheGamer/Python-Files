while True:
    try:
        score=int(input("Enter your score "))
        break
    except:
        print("Invalid Entry")

    
if score>100:
    print("It is a century")

elif score<100:
    print("It is not a century")

elif score==100:
    print("It is a century")


    
