from pymongo import MongoClient

MONGO_URI = "YOUR_MONGODB_ATLAS_CONNECTION_STRING"

client = MongoClient(MONGO_URI)

db = client["gradeflow_db"]

student_collection = db["students"]


def insert_student(student_data):
    result = student_collection.insert_one(student_data)
    return result.inserted_id


def get_all_students():
    students = list(student_collection.find({}, {"_id": 0}))
    return students

def get_student(student_id):
    student = student_collection.find_one(
        {"student_id": student_id},
        {"_id": 0}
    )
    return student

def update_student(student_id, updated_data):
    result = student_collection.update_one(
        {"student_id": student_id},
        {"$set": updated_data}
    )
    return result.modified_count

def delete_student(student_id):
    result = student_collection.delete_one(
        {"student_id": student_id}
    )
    return result.deleted_count