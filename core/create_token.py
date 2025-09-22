from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
from sqlalchemy.orm import Session
from fastapi import Depends
from db.database import get_db
from models.user import User
from schemas.JWT import TokenData,Token
from fastapi import HTTPException,status

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30




def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception, db: Session):
  
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role:str =payload.get("role")
        print(payload)
        print(role)
        if email is None or role is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        print("hghghghggh")
        raise credentials_exception

    user = db.query(User).filter(User.email == token_data.email).first()
    if not user:
        print("lklklklkl")
        raise credentials_exception
    
    # user.role=role
    return user



