"""
Zachary Hunn
Assigment 6.2

"""

# Imports
from pymongo import MongoClient

# Database Connection

db_url = "mongodb+srv://admin:admin@cluster0.nsmhu.mongodb.net/test"

# Coonection to the DB
client = MongoClient(db_url)

db = client.pytech

# Get collection
students = db.pystudent

# Find all students and print

list_of_students = students.find({})

print("---- DISPLAYING THE LIST OF STUDENTS ----")

for student in list_of_students:
    print(f" Student ID: {student['student_id']} \n First Name: {student['first_name']} \n Last Name: {student['last_name']} \n")


# update student record
update_student = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "James"}})

#find one student

zachary = students.find_one({"student_id": "1007"})

# Print Student that has been updated
print("---- DISPLAYING STUDENT 1007 ----")

print(f" Student ID: {zachary['student_id']} \n First Name: {zachary['first_name']} \n Last Name: {zachary['last_name']} ")