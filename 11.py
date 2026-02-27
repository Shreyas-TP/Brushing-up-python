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


student = [ "alice", "bob", "charlie", "dave", "eve" ]
marks = [ 85, 90, 78, 92, 88 ]

student_marks={}#creating an empty dictionary to store the student names and their marks
for i in range(len(student)):#looping through the list of students and marks using the index
    student_marks[student[i]]=marks[i]#adding the student name as the key and the corresponding mark as the value in the dictionary
print(student_marks)


student_marks={}
for i in range(1, len(student)):#looping through the list of students and marks using the index, starting from index 1 and incrementing by 2 to access only the odd indices
    student_marks[student[i]]=marks[i]#adding the student name as the key and the corresponding mark as the value in the dictionary

print(student_marks)



#list comprehension
l=[x for x in range(1,11) if x%2==0]
print (l)
squared=[i**2 for i in l]#creating a new list called squared by iterating through each element i in the list l and calculating its square (i**2) and adding it to the new list squared
print(squared)
divied_by_2=[i/2 for i in l]#creating a new list called divided_by_2 by iterating through each element i in the list l and dividing it by 2 (i/2) and adding it to the new list divided_by_2
print(divied_by_2)

name=["Shreyas", "Ananya", "Rohan", "Dave", "Eve"]
first_letter=[i[0] for i in name]#creating a new list called first_letter by iterating through each element i in the list name and accessing the first character of each name (i[0]) and adding it to the new list first_letter
print(first_letter)

#dictionary comprehension

name=["Shreyas", "Ananya", "Rohan", "Dave", "Eve"]
d={i:len(name) for i in name}#creating a new dictionary called d by iterating through each element i in the list name and using the element as the key and the length of the element (len(i)) as the value in the new dictionary d
l={i:len(i) for i in name}

print(d)
print(l)

students_marks={"Shreyas": 85, "Ananya": 90, "Rohan": 78}
squared_marks={student: marks**2 for student, marks in students_marks.items()}#creating a new dictionary called squared_marks by iterating through each key-value pair in the students_marks dictionary and calculating the square of the marks and adding it to the new dictionary squared_marks with the same student name as the key
print(squared_marks)

city_population = {
    "Bengaluru": 184,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city:p for city, p in city_population.items() if p > 10 and p<100}#creating a new dictionary called large_cities by iterating through each key-value pair in the city_population dictionary and adding the city and its population to the new dictionary large_cities only if the population is greater than 10 and less than 100
print(large_cities)


#Splitting Strings to Create Lists

sentence = "Hello, how are you doing today?"
words = sentence.split()#splitting the sentence into a list of words using the split() method
print(words)

x=input("enter a number: ")
print(x)
print(x.split())
l=[int(x) for x in x.split()]
print(l)

#direct input and splitting it into a list of integers
y= [int(x) for x in input("enter a number: ").split()]
print(y)