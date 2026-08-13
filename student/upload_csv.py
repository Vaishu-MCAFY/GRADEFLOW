import csv
from .mongodb import insert_student

def upload_students_from_csv(file_path):
    """
    Reads student data from CSV file
    and inserts it into MongoDB.
    """

    count = 0

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            student = {
                "student_id": row["student_id"],
                "name": row["name"],
                "email": row["email"],

                # Store subject marks in a List
                "marks": [
                    int(row["python"]),
                    int(row["java"]),
                    int(row["dbms"])
                ],

                "percentage": float(row["percentage"]),
                "rank": int(row["rank"])
            }

            insert_student(student)
            count += 1

    return count