from fastapi import APIRouter, Depends, HTTPException, status
from classes import schemas_dto
import uuid
from typing import List
from documentation.description import api_description


router = APIRouter(
    prefix='/students',
    tags=['students']
)

students = [
    schemas_dto.Student(id="1", name="Adama"),
    schemas_dto.Student(id="2", name="Adrien"),
    schemas_dto.Student(id="3", name="Akbar")
]

# Verbs + Endpoints
@router.get('', response_model=List[schemas_dto.Student])
async def get_student():
    return students

# 1. Exercice (10min) Create Student POST
# response_model permet de définir de type de réponse (ici nous retournons le student avec sont id)
# status_code est définit sur 201-Created car c'est un POST
@router.post('', response_model=schemas_dto.Student, status_code=201)
async def create_student(givenName: str):
    # génération de l'identifiant unique
    generatedId = uuid.uuid4()
    # création de l'object/dict Student avec les données reçues
    newStudent = schemas_dto.Student(id=str(generatedId), name=givenName)
    # Ajout du nouveau Student dans la List/Array
    students.append(newStudent)
    # Réponse définit par le Student avec son ID
    return newStudent

# 2. Exercice (10min) GET by ID
# response_model est un Student car nous souhaitons trouvé l'étudiant correspodant à l'ID
@router.get('/{studentId}', response_model=schemas_dto.Student)
async def get_student_by_id(studentId: str):
    #On parcours chaque étudiant de la liste
    for student in students:
        # Si l'ID correspond, on retourne l'étudiant trouvé
        if student.id == studentId:
            return student
        # pas de "else" car si on ne l'a pas trouvé, on continue avec le prochain student
    # Si on arrive ici, c'est que la boucle sur la liste "students" n'a rien trouvé
    # On lève donc un HTTP Exception avec un message d'erreur
    raise HTTPException(
 status_code=404, detail=f"Student {id} not found."
 )

# 3. Exercice (10min) PATCH Student (name)
@router.patch('/{studentId}', status_code=204)
async def patch_student(studentId: str, newName: str):
    #On parcours chaque étudiant de la liste
    for student in students:
        # Si l'ID correspond, 
        if student.id == studentId:
            # On modifie le nom
            student.name = newName
            return
        # pas de "else" car si on ne l'a pas trouvé, on continue avec le prochain student
    # Si on arrive ici, c'est que la boucle sur la liste "students" n'a rien trouvé
    # On lève donc un HTTP Exception avec un message d'erreur
    raise HTTPException(
 status_code=404, detail=f"Student {id} not found."
 )

# 4. Exercice (10min) DELETE Student
@router.delete('/{studentId}', status_code=204)
async def delete_student(studentId: str):
    #On parcours chaque étudiant de la liste
    for student in students:
        # Si l'ID correspond, on retourne l'étudiant trouvé
        if student.id == studentId:
            # On supprime l'étudiant de la liste
            students.remove(student)
            return student
        # pas de "else" car si on ne l'a pas trouvé, on continue avec le prochain student
    # Si on arrive ici, c'est que la boucle sur la liste "students" n'a rien trouvé
    # On lève donc un HTTP Exception avec un message d'erreur
    raise HTTPException(
 status_code=404, detail=f"Delete student {id} failed, id  not found."
 )