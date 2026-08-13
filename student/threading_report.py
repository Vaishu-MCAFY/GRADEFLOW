import threading
from .reports import Report

def generate_report(student):
    try:
        report = Report(student)

        print("\n===================================")
        print("        STUDENT REPORT CARD")
        print("===================================")
        print("Student ID :", student.student_id)
        print("Name       :", student.name)
        print("Email      :", student.email)
        print("Department :", student.department)
        print("Semester   :", student.semester)

        print("\nSubject Marks")
        for subject, marks in student.subjects.items():
            print(f"{subject:<20} {marks}")

        print("\n-----------------------------------")
        print("Total       :", report.total())
        print("Average     :", report.average())
        print("Percentage  :", report.percentage())
        print("Highest     :", report.highest())
        print("Lowest      :", report.lowest())
        print("Grade       :", report.grade())
        print("Result      :", report.result())
        print("===================================")

    except Exception as e:
        print(f"Error generating report for {student.student_id}: {e}")


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

    print("\nAll Student Reports Generated Successfully.")