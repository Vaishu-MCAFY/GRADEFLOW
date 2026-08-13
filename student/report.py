import re


class InvalidMarksException(Exception):
    pass

class Student:

    def __init__(self, student_id, name, email, department, semester, subjects):

        self.student_id = student_id
        self.name = name
        self.email = email
        self.department = department
        self.semester = semester
        self.subjects = subjects

        self.validate()

    def validate(self):

        if not re.match(r"^STU\d{3}$", self.student_id):
            raise ValueError("Invalid Student ID")

        if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', self.email):
            raise ValueError("Invalid Email")

        for mark in self.subjects.values():
            if mark < 0 or mark > 100:
                raise InvalidMarksException("Marks must be between 0 and 100")

class Report:

    def __init__(self, student):
        self.student = student

    def total(self):
        return sum(self.student.subjects.values())

    def average(self):
        return round(self.total() / len(self.student.subjects), 2)

    def percentage(self):
        return round(self.average(), 2)

    def highest(self):
        return max(self.student.subjects.values())

    def lowest(self):
        return min(self.student.subjects.values())

    def grade(self):

        p = self.percentage()

        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 40:
            return "D"

        return "F"

    def result(self):

        if self.lowest() < 40:
            return "Fail"

        return "Pass"