# app/domain/user_repository.py
from abc import ABC, abstractmethod
from .user import User
from typing import Optional

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        pass
