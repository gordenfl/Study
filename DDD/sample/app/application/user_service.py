# app/application/user_service.py
from app.dto import RegisterUserDTO, UserResponseDTO
from app.domain.user import User
from app.domain.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, dto: RegisterUserDTO) -> UserResponseDTO:
        if self.user_repo.get_by_username(dto.username):
            raise ValueError("User already exists")

        user = User(dto.username, dto.email)
        self.user_repo.save(user)

        return UserResponseDTO(id=user.id, username=user.username, email=user.email)
