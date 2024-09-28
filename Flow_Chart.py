year=int(input("Enter a year"))
if year%4!=0:
    print("It is a common")
elif year%100!=0:
    print("It is Leap year")
elif year%400!=0:
    print("It's a common year")
else:
    print("It is a Leap year")
    
