name=(input("enter the name of the worker:"))
category=(input("enter the category of the worker: "))
daysworked=int (input("enter the number of days worked:"))
if category=="A":
    if daysworked==25: print("daily_pay:900") 
elif daysworked<25:
    print("daily pay:750")
else:
 print("extra pay:1500")
if category=="B":  
 if daysworked==25:
     print("daily pay:600")
elif daysworked<25:
    print("daily pay:450")
else:
    print("daily pay:1200")
    if category=="C":
        if daysworked==25:
            print("daily pay:200")
    elif daysworked<25:
        print("daily pay:100")
    else:
        print("daily pay:900")
    