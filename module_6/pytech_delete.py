"""
Zachary Hunn 
Assignment 6.3
"""

# Imports
from pymongo import MongoClient


# Database URl
db_url = "mongodb+srv://admin:admin@cluster0.nsmhu.mongodb.net/test"

# Database Connection

client = MongoClient(db_url)

# connect to pytech

db = client.pytech

# get students 

students = db.pystudent

#find all students

list_of_students = students.find({})
for student in list_of_students:
    print(f" Student ID: {student['student_id']} \n First Name: {student['first_name']} \n Last Name: {student['last_name']} \n")


# New Student Document

new_student = {
    "student_id": "1010",
    "first_name": "Zaria",
    "last_name": "Hunn"  
} 

# Insert New Student
print("---- INSERTING NEW STUDENT INFORMATION ----")
zaria_id = students.insert_one(new_student).inserted_id

print(f"\nInsert student record Zaria Hunn into the student collection with document_id {str(zaria_id)}\n")

# Finrd one student

zaria = students.find_one({"student_id": "1010"})

print("---- DISPLAY STUDENT DOCUMENT FROM QUERY ----")

print(f"Student ID: {zaria['student_id']} \n First Name: {zaria['first_name']} \n Last Name: {zaria['last_name']} \n")

#Delete student

deleted_student = students.delete_one({"student_id": "1010"})

print("---- DISPLAYING LIST OF STUDENTS ----")
new_list = students.find({})

for student in new_list:
    print(f" Student ID: {student['student_id']} \n First Name: {student['first_name']} \n Last Name: {student['last_name']} \n")
