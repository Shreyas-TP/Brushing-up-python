#class and objects

class Car:
    #attributes
    def __init__ (self, brand, model):
        self.brand = brand #instance variable
        self.model = model #instance variable

    #methods
    def display_info(self):
        print(f"The car brand is {self.brand} and the model is {self.model}")
    
#creating object of the class
car1=Car("Bmw", "M4")
car2=Car("lambo", "Aventodor")

#calling functions
car1.display_info()
car2.display_info()



#practice
class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price=price
    def display(self):
        print(f"The barnd of mobile is : {self.brand} and the price is : {self.price}.")

m1=mobile("REDMI","8000")
m2=mobile("Mi","13000")
m3=mobile("ONEPLUS","25000")

m1.display()
m2.display()
m3.display()