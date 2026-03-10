#getters and setters


class Student:
    def __init__(self, name, age):
        self.name=name
        self.__age=age #private attribute

    #getter for name
    def get_name(self):
        return self.name
    
    #setter for age
    def set_name(self, name):
        self.name=name

    #getter for age
    def get_age(self):
        return self.__age
    
    #setter for age
    def set_age(self, age):
        if isinstance(age, int):
            self.__age=age
        else:
            print("error")

s=Student("Shreyas", 21)
#s.set_age("dadas")#validation error
print(s.get_name())
print("Age:", s.get_age())
s.set_name("shivu")
s.set_age(22)
print(s.get_name())
print("updated age:", s.get_age())

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student("Anita", 20)
print("Age:", student.get_age())  # Accessing age with getter
student.set_age(21)  # Modifying age with setter
print("Updated Age:", student.get_age())


#method overloading

class Mathop:
    def add(self, a, b, c=0):#here c is a default value if c parmeter is not passed it will skip dont give error
        return a+b+c
math=Mathop()
print(math.add(1,2))
print(math.add(1,2,3))
'''
#method overriding

class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
animal=Animal()
animal.sound()
animal2=Dog()
animal2.sound()
'''
#super() funnction
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        self.name=name

    def sound(self):
        super().sound()
        print(f"{self.name} is barking")

    def get_angry(self):
        self.sound()


animal2=Dog("tommy")
animal2.sound()
animal2.get_angry()

#abstract class
from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehical):
    def __init__(self, name):
        self.name=name

    def start_engine(self):
        print("staring engine...")
    
b=Bike("Z900")
print(b.name)
        

        
#practice

#Getters and Setters:
class BankAccount:
    def __init__(self, balance):
        self.__balance=balance

    def get_balance(self):
        print(self.__balance)

    def set_balance(self, balance):
        self.__balance=balance

bal=BankAccount(4000)
bal.get_balance()
bal.set_balance(5000)
bal.get_balance()

#Method Overloading:
class Calculator:
    def multiply(self, a, b, c=0):
        return a*b*c
    
mul=Calculator()
print(mul.multiply(2,2,2))
print(mul.multiply(2,3,4))
    
#Method Overriding:

class Shape:
    def draw(self):
        print("drawing shape")


class Circle(Shape):
    def draw(self):
        print("drawing circle")

drawing=Circle()
drawing.draw()

#Abstract Classes:
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name=name
    @abstractmethod
    def claculate_salary(self):
        pass

    def display_info(self):
        print(f"Employee name = {self.name}")

        
class Manager(Employee):
    def __init__ (self, name, wh, rph):
        super().__init__(name)
        self.wh=wh
        self.rph=rph
    def claculate_salary(self):
        return self.wh * self.rph
emp=Manager("shreyas", 160, 2500)
emp.display_info()


sal=emp.claculate_salary()
print(f" calculated salary is {sal}")
