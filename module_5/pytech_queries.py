"""
    Zachary Hunn
    Assignment 5.3
"""

# Import Statement
from pymongo import MongoClient

db_url = "mongodb+srv://admin:admin@cluster0.nsmhu.mongodb.net/test"

# Cluster connection
client = MongoClient(db_url)

# Connect to pytech
db = client.pytech

# get student collection
students = db.pystudent

# find all students
list_of_students = students.find({})

print("Displaying  students documents from find() query")

for student in list_of_students:
    print(" Student ID: " + student["student_id"] + "\n  First Name: " + student["first_name"] + "\n  Last Name: " + student["last_name"] + "\n")


# find one student
zayden = students.find_one({"student_id": "1008"})

print("Displaying student document from find_one() query")

print(f"Student ID: {zayden['student_id']} \n First Name: {zayden['first_name']} \n Last Name: {zayden['last_name']}")