import hashlib


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def read_text_file(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as file:
        return file.read()
