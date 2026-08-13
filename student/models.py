class Student:
    def __init__(self, student_id, name, email, marks):
        self.student_id = student_id
        self.name = name
        self.email = email

        self.marks = marks

        self.percentage = sum(self.marks) / len(self.marks)

        self.rank = None

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "marks": self.marks,
            "percentage": round(self.percentage, 2),
            "rank": self.rank
        }


class Report:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student.to_dict())