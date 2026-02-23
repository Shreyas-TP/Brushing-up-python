#Logical Operator Practice

s1=int(input("Enter a ip: "))
s2=int(input("Enter a ip: "))
print((s1 and s2)>10)
res=((s1 or s2)>10)
print(not(res))

s1=int(input("Enter a ip: "))
s2=int(input("Enter a ip: "))   
print((s1<5 or s2<5))

print(not(s1>s2))
#Comparison Operator Challenge

age = int(input("Enter your age: "))
if age>=18:
    print("adult")
else:
    print("minor")


#Membership Operator Exercise:

str1=input("Enter a string: ")
print('s' in str1)

print('python' not in str1)


#Bitwise Operator Task

a=2
b=3
print(a & b)
print(a | b)    
print(a ^ b)
print(~a)
print(a << 1)
print(b >> 1)
print(a << 2)
print(b >> 2)
