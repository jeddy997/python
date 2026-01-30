name=str(input("enter the name:"))
admno=int(input("enter admno:") ) 
meal_type=str(input("enter meal type(breakfast,lunch,supper:)"))
mealcost=int (input("enter meal cost:"))
balance=float (input("enter remaining balance:"))   
mealprice={"breafast":100,"lunch":200,"supper":250}
if meal_type not in mealprice:  
    print("invalid meal entered")
else:
    price=mealprice[meal_type]   
    if balance<price:
        print("transaction denied due to insufficient funds")
    else:
        balance-=price
        print("f/n....fee payment recipt")
        print(f"name:{name}")
        print (f"admno:{admno}")
        print(f"meal type:{meal_type}")
        print(f"meal price:{mealprice}")
        print(f"balance:{balance}")
        if balance<150:
            print("AI adivice:low balance please top up")
        else:
            print("AI advice:mantain weekly top up schedule")
        