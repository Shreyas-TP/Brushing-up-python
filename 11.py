#Comprehension is a concise way to create lists, dictionaries, sets, and generators. 
# It allows you to generate a new collection by applying an expression to each item
#  in an iterable, optionally filtering items using a condition.


#looping through a list and calculating the total
l=[1,2,3,4,5]
total=0

for i in l:
    print(total)
    total+=i
print(total)


#looping through a dictionary and printing the key-value pairs
students_marks={"Shreyas": 85, "Ananya": 90, "Rohan": 78}

for i in students_marks.keys():
        print(i)
for i in students_marks.values():
        print(i)
for student, marks in students_marks.items():
    
    print(f"{student} scored {marks} marks")    