#conditional statements
'''
a=12
if a%2 !=0:
    print("odd")
else:    
    print("even")

if a<=10:
    print("a is less than or equal to 10")

else:
    print("a is greater than 10")


age=float(input("enter your age: "))
if age<18:
    print("you get a student membership.")
elif age>=60:
    print("you get a senior citizen membership.")
else:
    print("you get a regular membership.")
        
 '''

from time import time


time=float(input("enter the time in 24 hour format: "))

if time>=8 and time<=9.30:
    print("breakfast time")
elif time>=12.30 and time<13.30:
    print("lunch time")
elif time>=20.30 and time<=22:
    print("dinner time")
else:
    print("invalid time to take meal")