#simple calci
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def display_menu():
    print("Simple calculator")
    print("1.add\n2.sub\n3.mul\n4.div\n5.exit")

while(True):
    display_menu()
    
    choice=int(input("Enter you choice : "))
    if choice in {1,2,3,4}:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))

        if choice==1:
            print(f"the addition of {a} and {b} is ", add(a,b))
        elif choice==2:
            print(f"the subtraction of {a} and {b} is ", sub(a,b))
        elif choice==3:
            print(f"the multiplication of {a} and {b} is ", mul(a,b))
        elif choice==4:
            print(f"the division of {a} and {b} is ", div(a,b))
    elif choice==5:
        print("Turned of...")
        break 
    else:
        print("Invalid Choice!! Try again ")
'''
#BAnking System menu driven
def menu():
    print("Simple Banking System")
    print("1.Check balance\n2.Deposite\n3.Withdraw\n4.Exit")
balance=0
while(True):
    menu()
    choice=int(input("Enter your choice :"))
    if choice==1:
        print("your balance is...", balance)
    elif choice==2:
        amount=int(input("enter amount to deposite :"))
        balance+=amount
        print("deposited successfully", amount)
    elif choice==3:
        amount = int(input("enter amount to withdrawl"))
        balance-=amount
        print("withdrawl amount is :", amount )
    elif choice==4:
        print("Exited")
        break
    
        
        



