from models.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException


def get_all_users(db:Session):
    db_user=db.query(User).filter(User.role=="user").all()

    if not db_user:
        raise HTTPException(status_code=404,detail="Users not Found")
    return db_user
    
    