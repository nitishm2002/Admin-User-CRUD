from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User


def delete_user(user_id:int,db:Session):
    db_user=db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(db_user)
    db.commit()

    return "user deleted successfully"