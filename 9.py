#while loops

'''
is_failed = True
i = 1

while is_failed:
    if i%2!=0:
        i += 1
        continue
    print(f"try {i}")
    i+=1
    if i>=100:
        break
print("you failed")

i=0
while i<=10:
    print(f"{i} shreyas")
    i+=1

#nested while loop

i=0
while i<=10:
    j=0
    while j<i:
        print("shreyas ", end="")
        j+=1
    print("")
    i+=1

pin=1234
trails=1
while trails<=3:
    enter_pin=int(input(f"trails-{trails} enter the pin: "))
    if enter_pin==pin:
        print("you are logged in")
        break
    else:
        print("invalid pin")
        trails+=1
    if trails>3:
        print("maximum trails reached, try again later")

        

i=0
while i<=20:
    if i%2!=0:
        print(i)
    i+=1

seats=8
while seats>=0:
    print(f"available seats: {seats}")
    book_seats=int(input("enter the number of seats you want to book: "))
    if book_seats<=seats:
        print(f"{book_seats} seats booked successfully")
        seats-=book_seats
    else:
        print("not enough seats available")'''

countdown=10
while countdown>=1:
    print(countdown)
    countdown-=1
print("happy new year")

