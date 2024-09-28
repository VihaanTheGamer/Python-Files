def is_leap(year):
    

    if year%4!=0:
        return False
        #print("It is a common")
    elif year%100!=0:
        return True
        #print("It is Leap year")
    elif year%400!=0:
        return False
        #print("It's a common year")
    else:
        return True
        #print("It is a Leap year")


year=int(input("Enter a year "))






month=input("Enter a month ").capitalize()
if month=="January":
    print("There are 31 days")
elif month== "February":
    if is_leap(year):
        print("29 days")
    else:
        print("28 days")
    
elif month=="March":
    print("There are 31 days")
