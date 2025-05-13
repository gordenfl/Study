# app/domain/user.py
import uuid

class User:
    def __init__(self, username: str, email: str):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
