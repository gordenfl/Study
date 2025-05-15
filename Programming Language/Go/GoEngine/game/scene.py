# game/scene.py
class SceneManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user_obj):
        self.users[user_obj.user_id] = user_obj
        print(f"[Scene] User {user_obj.user_id} entered scene.")

    def move_user(self, user_id, dx, dy):
        user = self.users.get(user_id)
        if user:
            user.move(dx, dy)
