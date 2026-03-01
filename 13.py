#lambda functions
#lambda functions are anonymous functions that can have any number of arguments, 
# but can only have one expression. They are often used for short, 
# simple functions that are not reused elsewhere in the code.
'''
#variable lenth arguments
#*args allows you to pass a variable number of non-keyword arguments to a function.
def add(*num):
    print(sum(num))
add(1, 2, 3, 4)


def addd(*num):
    return sum(num)
print(addd(1, 2, 3, 4))


def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4,55))

#**kwargs allows you to pass a variable number of keyword arguments to a function.
def student_info(**info):
    for key, value in info.items():
        print(f"{key} --- {value}")
student_info(name="John", age=25, city="New York", grade="A")


#lambda functions
add = lambda x, y: x + y
print(add(5, 3))

multiply = lambda x, y: x * y
print(multiply(5, 3))

double = lambda x: x * 5
print(double(5))

#for dictionary
std_marks = [{'name': 'John', 'marks': 85}, {'name': 'Alice', 'marks': 90}, {'name': 'Bob', 'marks': 78}]
sorted_marks = sorted(std_marks, key=lambda x: x["marks"], reverse=True )
print(sorted_marks)
'''

#Recusion

def greet():
    print("Hello, World!")
    greet()# This will cause a RecursionError: maximum recursion depth exceeded

def factorial(n):
    if n==1:# Base case: the factorial of 1 is 1
        return 1# Recursive case: the factorial of n is n multiplied by the factorial of n-1
    return n * factorial(n-1)  # This will calculate the factorial of n by calling itself with n-1 until it reaches the base case
print(factorial(5))# This will print 120, which is the factorial of 5 (5 * 4 * 3 * 2 * 1)