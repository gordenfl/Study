# app/infrastructure/in_memory_user_repo.py
from app.domain.user_repository import UserRepository
from app.domain.user import User

from typing import Optional

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def save(self, user: User):
        self.users[user.username] = user

    def get_by_username(self, username: str) -> Optional[User]:
        return self.users.get(username)
