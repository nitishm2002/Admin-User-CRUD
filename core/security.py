from passlib.context import CryptContext
import secrets
import string

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash:

    def hash_password(password:int):
        return pwd_cxt.hash(password)
    
    def verify_password(plain_password:str,hash_password:str):
        return pwd_cxt.verify(plain_password,hash_password)


def generate_password(length=12):
    characters=string.ascii_letters + string.digits +string.punctuation
    password="".join(secrets.choice(characters) for _ in range(length))
    return password