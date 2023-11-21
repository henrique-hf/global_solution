import util
from util import *


class User:
    def __init__(self, user_id: str, password: str):
        self.user_id = user_id
        self.hashed_password = util.hash_password(password)

    def authenticate(self, password: str) -> bool:
        if util.hash_password(password) == self.hashed_password:
            return True
        else:
            return False

# salvar o resulta do gpt { (user_id, timestamp): str} ou salvar dentro próprio usuário