import math
import statistics

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return round(percentage, 2)

def generate_analytics(students):

    if not students:
        return {
            "students": [],
            "total_students": 0,
            "average": 0,
            "highest": 0,
            "lowest": 0,
            "topper": "",
            "at_risk_students": []
        }

    for student in students:
        student["percentage"] = calculate_percentage(student["marks"])

    percentages = [student["percentage"] for student in students]

    average = statistics.mean(percentages)
    highest = max(percentages)
    lowest = min(percentages)

    average = math.floor(average * 100) / 100

    students.sort(
        key=lambda student: student["percentage"],
        reverse=True
    )

    for index, student in enumerate(students, start=1):
        student["rank"] = index

    topper = students[0]["name"]

    at_risk_students = [
        student
        for student in students
        if student["percentage"] < 40
    ]

    return {
        "students": students,
        "total_students": len(students),
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "topper": topper,
        "at_risk_students": at_risk_students
    }