from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schemas import ChangePassword
from core.security import Hash

def change_password(data:ChangePassword,db:Session,current_user:User):
    db_user=db.query(User).filter(User.email==current_user.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="user Not Found")
    if data.new_password!=data.confirm_password:
        raise HTTPException(status_code=403,detail="passowrd and confirm passowrd should be same.")
    if db_user.first_login==True:
        db_user.password=Hash.hash_password(data.new_password)
        db_user.first_login=False
        db.commit()
        db_user.first_login=False

        return "password changed successfully"
    return "this is only when user login first time.if you are not loging first time then use reset password API."


    

    
    

    