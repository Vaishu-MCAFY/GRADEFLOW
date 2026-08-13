import threading
from .reports import Student, Report


def generate_report(student):

    report = Report(student)

    print("\n==============================")
    print("STUDENT REPORT")
    print("==============================")

    print("Student ID :", student.student_id)
    print("Name       :", student.name)
    print("Email      :", student.email)
    print("Department :", student.department)
    print("Semester   :", student.semester)

    print("\nSubject Marks")

    for subject, marks in student.subjects.items():
        print(subject, ":", marks)

    print("\nTotal      :", report.total())
    print("Average    :", report.average())
    print("Percentage :", report.percentage())
    print("Highest    :", report.highest())
    print("Lowest     :", report.lowest())
    print("Grade      :", report.grade())
    print("Result     :", report.result())


def generate_reports(students):

    threads = []

    for student in students:

        t = threading.Thread(
            target=generate_report,
            args=(student,)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All Reports Generated Successfully")