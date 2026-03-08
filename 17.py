# Encapsulation and Abstraction

class Database:
    def __init__(self):
        self.__students={} #__ used private attribute because for security, if we private attribute we cannt access the attribute directly
    
    def write(self, key, value): #this fuction is to store the key value pairs in created student dictionary
            self.__students[key]=value
    
    def read(self, key): # only key is enough cause we are fetching the db
        if key in self.__students:
            print(self.__students[key])
        else:
             print("requeste data not found")

db=Database()
db.write("shreyas", "BE")
db.write("shree", "B.tech")

db.read("shreyas")
db.read("shree")


#encapsulation (security and maintainability) pratice

class BankAccount:
    def __init__(self, accno, balance):
        self.__accno=accno
        self.__balance=balance

    def check_balance(self, balance):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

sbi=BankAccount(123, 20000)
sbi.check_balance(123)
sbi.deposit(98000)
sbi.check_balance(123)
sbi.withdraw(18000)
sbi.check_balance(123)

#print(sbi.__balance)    #cannot access directly cause its private attribute
    
#Abstraction
class Phone:
    def __init__(self, owner):
        self.owner = owner
        # Internal: Simplified representation of contacts
        self._contacts = {"Mom": "555-0101", "Work": "555-0202"}
        # Internal: Camera state management
        self._camera_active = False

    def call_contact(self, name):
        """Simulates calling a contact by name."""
        number = self._contacts.get(name)
        if number:
            print(f"[{self.owner}'s Phone] Calling {name} ({number})...")
            print("..Connected.")
        else:
            print(f"[{self.owner}'s Phone] Error: Contact '{name}' not found.")

    def take_picture(self):
        """Simulates taking a picture, hiding initialization details."""
        print(f"[{self.owner}'s Phone] Initializing camera...")
        self._camera_active = True
        print("..Flash! Picture taken and saved to gallery.")
        self._camera_active = False

# Example Usage
my_phone = Phone("Alice")
my_phone.call_contact("Mom")
my_phone.take_picture()



# Inheritance


class Vehicle:  # Fixed typo
    def __init__(self, make):  # Renamed 'start' to 'make' for clarity (avoiding conflict)
        self.make = make
    def start_engine(self):  # Renamed method to avoid attribute conflict
        print("Vehicle has started")

class Bike(Vehicle):
    def ride(self):  # Removed unused 'start' parameter
        print(f"Riding the {self.make}")  # Adjusted print for clarity
        
v = Bike("Z900")
v.start_engine()  # Updated call
v.ride()  # Now works without extra argument

#Polymorphism
#Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area. 
# Each class should calculate area differently based on its shape.
#Create a loop to calculate areas for both Circle and Rectangle objects.
import math

class Shape:
    """
    A base class for all shapes, defining the interface for area calculation.
    """
    def calculate_area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement the calculate_area method.")

class Circle(Shape):
    """
    Represents a circle and calculates its area using pi * r^2.
    """
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """
        Calculates the area of the circle.
        """
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    """
    Represents a rectangle and calculates its area using width * height.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

# --- Demonstration Loop ---

# Create a list of different shape objects
shapes = [
    Circle(radius=5),
    Rectangle(width=4, height=10),
    Circle(radius=1.5),
    Rectangle(width=6, height=6)
]

print("Calculating areas for various shapes:")

# Loop through the list and call the calculate_area method for each object
for i, shape in enumerate(shapes):
    area = shape.calculate_area()
    # The type() function is used for descriptive printing
    print(f"Shape {i+1} ({type(shape).__name__}): Area = {area:.2f}")

