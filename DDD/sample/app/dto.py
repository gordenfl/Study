# app/dto.py
from pydantic import BaseModel

class RegisterUserDTO(BaseModel):
    username: str
    email: str

class UserResponseDTO(BaseModel):
    id: str
    username: str
    email: str

