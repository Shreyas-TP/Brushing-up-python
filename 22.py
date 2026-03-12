#Error and Exception handling
'''
a=int(input("1st no:  "))
b=int(input("2nd no: "))
try:
    print(a/b)
except Exception as e:# it will give whichever error is occuring - errors are stored in Exception class= Built-in
    print("Error: 2", e)
else:
    print("error not occured...")
finally:
    print("whatever!!")

#we can also use specified error , if we only require to catch that specific error
#Catching Division by Zero
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
#Using finally
try:
    file = open("myfile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file... (even if error occurred)")

#using raise method
try:
    boy=input("enter the boy name :")
    if boy.lower()==("shreyas"):#useed .lowe() because of case issues
        print("Shreyas is readyy")
    else:
        raise Exception("you can only marry shreyas")
except Exception as e:# raise Exception is called here
    print("Error : ", e)

#practice
try:
    age = input("Enter your age: ")
    age = int(age)
    print(f"Your age is {age}")
except ValueError:
    print("Exception: It's not an integer")

'''

try:
    a=int(input("enter 1st no."))
    b=int(input("enter 2nd no."))
    div=(a/b)
    print("Result :", div)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")





