from fastapi import APIRouter


persona = APIRouter()

@persona.get("/personas")

def helloworldId():
    return "Hello World"