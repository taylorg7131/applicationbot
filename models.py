from flask_login import UserMixin

# Simple in-memory user store
users = {}

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        return users.get(user_id)

    @staticmethod
    def find_by_username(username):
        for user in users.values():
            if user.username == username:
                return user
        return None

    @staticmethod
    def register(id, username, password):
        users[id] = User(id, username, password)
