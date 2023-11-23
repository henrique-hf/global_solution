from src.user import User
import json
from src.AVLTree import AVLTree


class UserList:
    def __init__(self, users_tree=None):
        if users_tree is None:
            users_tree = AVLTree()
        self.users_tree = users_tree

    def add_user(self, user: User) -> bool:
        if self.get_user(user.user_id) is None:
            self.users_tree.insert(user.user_id, user)
            return True
        else:
            return False

    # def is_user_id_unique(self, user_id: str) -> bool:
    #     return user_id not in self.user_dict.keys()

    def get_user(self, user_id: str) -> User | None:
        result = self.users_tree.search(user_id)
        if result[0] is not None:
            return result[1]
        return None

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
            self.add_user(user)
