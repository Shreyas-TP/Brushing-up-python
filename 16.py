#Constructors and the self Keyword

class Movie:
    def __init__ (self, title, rating):
        self.title=title
        self.rating=rating
    def info(self):
        print(f"Movie {self.title} has {self.rating} rating.")

mov1=Movie("KGF 1", 8.5)
mov2=Movie("KGF 2", 9.5)

mov1.info()
mov2.info()


class Employee:
    def __init__(self, name, role, salary="30000"):
        self.name=name
        self.role=role
        self.salary=salary

    def display_info(self):
        print(f"This Employee {self.name} is {self.role} and has a Salary of {self.salary}")

    def display_name_role(self):
        print(f"This Employee {self.name} is {self.role}")

emp1=Employee("Shreyas", "SDE")
emp2=Employee("Alex", "Tester")

emp1.display_info()
emp2.display_info()

emp1.display_name_role()
emp2.display_name_role()