# Import du framework
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

# Initialisation de l'API
app = FastAPI(
    title="Attendance Tracker"
)

# Model Pydantic = Datatype
class Student(BaseModel):
    id: str
    name: str

students = [
    Student(id="1", name="Adama"),
    Student(id="2", name="Adrien"),
    Student(id="3", name="Akbar")
]

# Verbs + Endpoints
@app.get('/students', response_model=List[Student])
async def get_student():
    return students

# 1. Exercice (10min) Create Student POST
@app.post('/students', response_model=Student, status_code=201)
async def create_student(givenName: str):
    generatedId = uuid.uuid4()
    newStudent = Student(id=str(generatedId), name=givenName)
    students.append(newStudent)
    return newStudent

# 2. Exercice (10min) GET by ID
@app.get('/students/{studentId}', response_model=Student)
async def get_student_by_id(studentId: str):
    for student in students:
        if student.id == studentId:
            return student
    return None

# 3. Exercice (10min) PATCH Student (name)
@app.patch('/students/{studentId}', response_model=Student)
async def patch_student(studentId: str, newName: str):
    for student in students:
        if student.id == studentId:
            student.name = newName
            return student
    return None

# 4. Exercice (10min) DELETE Student
@app.delete('/students/{studentId}', response_model=Student)
async def delete_student(studentId: str):
    for student in students:
        if student.id == studentId:
            students.remove(student)
            return student
    return None

# Spécification...
# "Students" auront des "Attendances" pour des "Sessions"
# Utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... "Center" -> Sessions + Students -> Attendances
