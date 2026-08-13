import re

def validate_student_id(student_id):

    pattern = r"^ST\d{3}$"

    if re.match(pattern, student_id):
        return True

    return False

def validate_email(email):

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True

    return False

def validate_student(student_id, email):

    if not validate_student_id(student_id):
        return False, "Invalid Student ID"

    if not validate_email(email):
        return False, "Invalid Email Address"

    return True, "Validation Successful"