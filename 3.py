'''Boy = input("Enter the name of the boy: ")
Girl = input("Enter the name of the girl: ")

print(Boy + " Loves " + Girl) #concatenation of strings

#repetition of strings
boy= Boy
print(boy*3)'''

'''#String methods
text="Hello world "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Hello", "hi"))

#slicing
print(text[-2])
print(text[1:])
print(text[:7])
print(text[2:7])
print(text[1:8:2])

#escape sequence
print("shreyas\ntp")
print("shreyas\ttp")

print("This will print on two lines: Line 1\\nLine 2")


#practice
name=input("Enter your name: ")
age= int(input("age: "))

print(" hey " + name + " your age is " + str(age))
print(f"hii {name} you are {age} years old ")'''

#String Manipulation Exercise
story=input("Enter a story: ")
print(story)
print(story.upper())
print(story.lower())
print(story.replace(" ", "_"))
print(story.strip())

print(len(story))
exluding_spaces= len(story.replace(" ", ""))
print("Length excluding spaces: ", exluding_spaces)


print("hello \n\tworld and \\everyone")