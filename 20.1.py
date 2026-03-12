#student report card

class Student:
    def __init__(self, roll_no, name):
        self.roll_no=roll_no
        self.name=name
        self.__marks={}
    
    def add_marks(self, subject, marks):
        self.__marks[subject]=marks

    def get_marks(self):
        return self.__marks

    def calculate_avg(self):
        total=0
        for mark in self.__marks.values():
            total+=mark
        avrage=total/len(self.__marks)
        return avrage

    def is_passed(self):
        has_passed= all(mark>35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has Failed.")

    def calculate_grade(self):
        print("------------------------")
        print("Grade : ", end="")
        # TODO fix this
        if self.calculate_avg() >=85:
            print(f"{self.name} got Distinction.")
        elif self.calculate_avg() >=65 :
            print(f"{self.name} got First class.")
        elif self.calculate_avg() >=35 :
            print(f"{self.name} got Second class.")
        else:
            print(f"{self.name} has Failed.")

class ReportGenarator:
    @staticmethod
    def genarate(student: Student):
        student_marks=student.get_marks()
        print("------------------------")
        print(f"Student : {student.name}\nRoll_No : {student.roll_no}")
        print("---------Marks----------")
        for subject, marks in student_marks.items():
            print(f"{subject} --- {marks}")
        print("------------------------")
        print(f"Avrage : {student.calculate_avg()}")
        student.is_passed()
        student.calculate_grade()
        


              
s1=Student(66, "Shreyas")
s1.add_marks("SE", 95)
s1.add_marks("FSD", 55)

ReportGenarator.genarate(s1)


