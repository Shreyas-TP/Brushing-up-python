#for loops

'''
for i in range(1,11):
    print(i)#is the loop variable which takes the value from 1 to 10 in each iteration



for i in range(1,21,2):#range(start,stop,step)
    
    print(i, end=", ") #end is used to print in the same line with space


#nested for loop
for i in range(1,6):
    for j in range(1,11):#nested loop for multiplication table
        print(f"{i} x {j} = {i*j}")
    print("")

#break and continue statements in for loop
city=["mumbai","delhi","kolkata","chennai"]
for i in city:
    if i=="delhi":
        continue #skip the current iteration and move to the next iteration
    if i=="kolkata":
        print("kolkata is found")
        break#exit the loop when the condition is met
    print(i)


#iterating through a string using for loop
name = "Shreyas"
for i in name:
    print(i)
   
    
#enumerate function in for loop
name = "Shreyas"
for index, value in enumerate(name):
    print(f"index: {index}, value: {value}")
 
#else statement in for loop
for i in range(1,6):
    if i==6:
        print("three is found")
        break
    print(i)
else:
    print("loop is completed")


for i in range(200,2010):
    for j in range(1,11):
        print (f"{i} x {j} = {i*j} ")
    print(" ")

    
#dictionary iteration using for loop
student={"name":"shreyas","age":21,"course":"python"}
for key, value in student.items():#items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
    print(f"{key}: {value}")

    '''

#practice
'''
for i in range(1,31):
    if i%3==0:
        print(i, end=" ")

#calculates the sum of numbers from 1 to 10

total=0
for i in range(1,11):
    total+=i
print(f"the sum of numbers from 1 to 10 is: {total}")

name = input("enter your name: ")
for i in name:
    print(i)
'''
#Count Vowels in a String
string = input("enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for i in string:
    if i in vowels:
        count+=1
print(f"count of vowels in the string is: {count}")

    
