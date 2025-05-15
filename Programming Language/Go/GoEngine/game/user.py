# game/user.py
class UserObject:
    def __init__(self, user_id, x=0, y=0):
        self.user_id = user_id
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"[User] {self.user_id} moved to ({self.x}, {self.y})")
