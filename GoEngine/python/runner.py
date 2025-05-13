# GoEngine/python/runner.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.user import UserObject
from game.scene import SceneManager

# 实例缓存
scene = SceneManager()

def create_user(user_id):
    user = UserObject(user_id)
    scene.add_user(user)
    return user

def move_user(user_id, dx, dy):
    scene.move_user(user_id, dx, dy)
