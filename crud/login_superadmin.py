
from fastapi  import HTTPException
from sqlalchemy.orm import Session
from pydantic import EmailStr
from schemas.user_schemas import UserLogin
from models.user import User
from core.security import Hash
from core.create_token import create_access_token

from fastapi.security import OAuth2PasswordRequestForm

def login_superadmin(data:OAuth2PasswordRequestForm,db:Session):

    db_user=db.query(User).filter(User.email==data.username).first()
    print(db_user)
    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    if not Hash.verify_password(data.password,db_user.password):
        raise HTTPException(status_code=401,detail="Incorrect Password")
    access_token=create_access_token(data={"sub":data.username,"role":"superadmin"})
    return {"access_token":access_token,"token_type":"bearer"}
           
