# Import du framework
from fastapi import FastAPI

# Import des routers
import routers.router_students

# Import de la description de l'API
from documentation.description import api_description

# Initialisation de l'API
app = FastAPI(
    title="Attendance Tracker",
    description=api_description
)

# Ajout des routers
app.include_router(routers.router_students.router)



# Spécification...
# "Students" auront des "Attendances" pour des "Sessions"
# Utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... "Center" -> Sessions + Students -> Attendances
