#lambda functions
#lambda functions are anonymous functions that can have any number of arguments, 
# but can only have one expression. They are often used for short, 
# simple functions that are not reused elsewhere in the code.

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4))

#Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))