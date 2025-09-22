from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User

def get_user(user_id:int,db:Session):
    db_user=db.query(User).filter(User.id==user_id).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    return db_user
    


