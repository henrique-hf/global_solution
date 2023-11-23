import src.util as util


class User:
    def __init__(self, user_id: str, password: str, name: str, gender: str, age: int):
        self.user_id = user_id
        self.hashed_password = util.hash_password(password)
        self.name = name
        self.gender = gender
        self.age = age
        self.symptoms = []

    def authenticate(self, password: str) -> bool:
        if util.hash_password(password) == self.hashed_password:
            return True
        else:
            return False

    def save_symptom(self, date, symptom: str, treatment: str):
        self.symptoms.append((date, symptom, treatment))
