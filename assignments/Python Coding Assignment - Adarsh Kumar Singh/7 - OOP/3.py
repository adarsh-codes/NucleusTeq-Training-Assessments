
class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []
    
    def add_grade(self,grade):
        if 0 <= grade <= 100:
           self.grades.append(grade)
        else:
           print("Invalid grade. Must be between 0 and 100.")
    def average_grade(self):
        print(f"Average grade of {self.name} is",(sum(self.grades)/len(self.grades)))

student = Student("Adarsh")
student.add_grade(90)
student.add_grade(94)
student.add_grade(99)
student.add_grade(100)
student.add_grade(91)
student.average_grade()