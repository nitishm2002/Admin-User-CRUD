from fastapi import Depends,HTTPException,status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from .create_token import verify_token
from sqlalchemy.orm import Session
from db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")



async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = verify_token(token,credentials_exception,db)
    if user.role != "user":   
        raise HTTPException(status_code=403, detail="Not authorized")
    print(user.role)
    return user

async def get_current_admin(token:Annotated[str, Depends(oauth2_scheme)],db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user=verify_token(token,credentials_exception,db)
    print(user.role)
    if user.role!="superadmin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admins Only"
        )
    return user