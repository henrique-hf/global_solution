from user import User


class UserList:
    def __init__(self):
        self.user_dict = {}

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
