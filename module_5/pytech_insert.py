"""
Zachary Hunn
Assignment 5.3
"""

# Import statement
from pymongo import MongoClient

# Database url
db_url = "mongodb+srv://admin:admin@cluster0.nsmhu.mongodb.net/test"

# Cluster connection
client = MongoClient(db_url)

# Connect to pytech 
db = client.pytech

#Student Documents

zachary ={
    "student_id": "1007",
    "first_name":"Zachary",
    "last_name":"Hunn",
    "enrollments":[
        {
          "term":"Spring",
          "gpa":"3.5",
          "start_date":"March 01, 2021",
          "end_date":"June 01, 2021",
          "courses":[
                {   
                    "course_id":"001",
                    "description":"Intro to Korean",
                    "instructor":"Professor Nam Dosan",
                    "grade":"A"

              },

              {
                  "course_id":"002",
                    "description":"Business Marketing",
                    "instructor":"Professor Park Sae-ro-yi",
                    "grade":"B",
              }
          ]  
     }
    ]
    
}


zayden = {
    "student_id": "1008",
    "first_name": "Zayden",
    "last_name": "Hunn",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.5",
            "start_date": "March 01, 2021",
            "end_date": "June 01, 2021",
            "courses": [
                {
                    "course_id": "001",
                    "description": "Intro to Korean",
                    "instructor": "Professor Nam Dosan",
                    "grade": "A"

                },

                {
                    "course_id": "002",
                    "description": "Business Marketing",
                    "instructor": "Professor Park Sae-ro-yi",
                    "grade": "B",
                }
            ]
        }
    ]
}


zamir ={
    "student_id": "1009",
    "first_name": "Zamir",
    "last_name": "Hunn",
    "enrollments": [
        {
            "term": "Spring",
            "gpa": "3.5",
            "start_date": "March 01, 2021",
            "end_date": "June 01, 2021",
            "courses": [
                {
                    "course_id": "001",
                    "description": "Intro to Korean",
                    "instructor": "Professor Nam Dosan",
                    "grade": "A"

                },

                {
                    "course_id": "002",
                    "description": "Business Marketing",
                    "instructor": "Professor Park Sae-ro-yi",
                    "grade": "B",
                }
            ]
        }
    ]
}

#get the pystudent collection
students = db.pystudent

print("Inserting the student information")

zachary_id = students.insert_one(zachary).inserted_id
print("\t Insert student record Zachary Hunn into students collection with document_id" + str(zachary_id))

zayden_id = students.insert_one(zayden).inserted_id
print("\t Insert student record Zayden Hunn into students collection with document_id" + str(zayden_id))

zamir_id = students.insert_one(zamir).inserted_id
print("\t Insert student record Zamir Hunn into students collection with document_id" + str(zamir_id))
