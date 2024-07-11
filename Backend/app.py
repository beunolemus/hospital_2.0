from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.usuarios_roles import usuario_roles

app=FastAPI(
    title="Hospital",
    description="API para el almacenamiento de informacipn de un Hospital"
)
app.include_router(user)
app.include_router(person)
app.include_router(usuario_roles)

print ("Hola bienvenido a mi backend")