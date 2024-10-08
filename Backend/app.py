from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.cirugia import cirugia_router
from routes.espacios import espacio
from routes.horarios import horarios 

from fastapi.middleware.cors import CORSMiddleware



app=FastAPI(
    title="Hospital ",
    description="API para el almacenamiento de informacipn de un Hospital"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde localhost:5173
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(cirugia_router)
app.include_router(horarios)
app.include_router(espacio)
print ("Hola bienvenido a mi backend")