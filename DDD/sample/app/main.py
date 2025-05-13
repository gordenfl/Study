# app/main.py
from fastapi import FastAPI, HTTPException, Depends
from app.dto import RegisterUserDTO, UserResponseDTO
from app.application.user_service import UserService
from app.infrastructure.in_memory_user_repo import InMemoryUserRepository

app = FastAPI()
repo = InMemoryUserRepository()
user_service = UserService(repo)

def get_user_service():
    return user_service

@app.post("/register", response_model=UserResponseDTO)
def register_user(dto: RegisterUserDTO, service: UserService = Depends(get_user_service)):
    try:
        return service.register_user(dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
