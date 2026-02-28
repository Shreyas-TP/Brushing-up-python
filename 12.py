#functions
'''
def greet():
    print("Hey there! Welcome")

greet()

def marry(boy, girl):#parameters
    print(f"boy is {boy} and girl is {girl}")
    print(f"{boy} is getting married with {girl}")

marry("Shreyas", "Ananya")#positional arguments

marry(boy="Shreyas", girl="Ananya")#keyword arguments is used to specify
#the arguments by their names, rather than their position in the function definition.
#  This allows for more flexibility and readability in the code.


def tables(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
tables(5)


#return statement in function
def add(a,b):
    return (a+b)

result = add(10,20)
print(result)
print(add(10,20))

#global and local variables
x=10 #global variable
def func():
    y=20 #local variable
    print(f"inside the function x: {x}, y: {y}")
func()
print(f"outside the function x: {x}")
#print(y) #error because y is a local variable and cannot be accessed outside the function

'''

#practice problems on functions
def greet(name):
    print(f"Hey {name}! Welcome")
greet("Shree")



def func(a,b):
    return a+b
print(func(10,20))
print(func(5,15))
   
#take only name as input and print the full name with a default sirname
name=input("enter your name: ")
def fullname(name, sirname="theetha"):
    return name + " " + sirname
print(fullname(name))#only name is provided, so the default sirname will be used





name =input("enther ur name: ")

def fullname(name, sirname="theetha"):#default parameter is used when we want to give a default value to a parameter in case the user does not provide a value for that parameter.
    return name + sirname
print(fullname(name))


