from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.espacios import espacio
from routes.cirugia import cirugia_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    title="Hospital ",
    description="API para el almacenamiento de informacipn de un Hospital"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes, puedes restringirlo a ciertos dominios si es necesario
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)


app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(espacio)
app.include_router(cirugia_router)

print ("Hola bienvenido a mi backend")