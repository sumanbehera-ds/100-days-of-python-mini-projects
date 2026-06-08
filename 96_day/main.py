# Student Grade Management System
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def calculate_total(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        return total

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return self.calculate_total() / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        else:
            return "D"

    def display_result(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.get_grade())


student = Student("Suman", 101)
student.add_mark("Python", 88)
student.add_mark("SQL", 82)
student.add_mark("ML", 91)
student.display_result()