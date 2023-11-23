from src.user import User
import json


class UserList:
    def __init__(self, user_dict=None):
        if user_dict is None:
            user_dict = {}
        self.user_dict = user_dict

    def add_user(self, user: User) -> bool:
        if self.is_user_id_unique(user.user_id):
            self.user_dict[user.user_id] = user
            return True
        else:
            return False

    def is_user_id_unique(self, user_id: str) -> bool:
        return user_id not in self.user_dict.keys()

    def get_user(self, user_id: str) -> User:
        return self.user_dict[user_id]

    def load_mocked_users(self, file_path: str):
        with open(file_path) as f:
            data = json.load(f)

        for e in data:
            user = User(
                e["user_id"],
                e["password"],
                e["name"],
                e["gender"],
                e["age"]
            )
            self.user_dict[e["user_id"]] = user
