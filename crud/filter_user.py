from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.user import User
from models.user_details import UserDetail
from fastapi import HTTPException

def filter_user(query:str,db:Session):
    users=db.query(User).join(UserDetail).filter(or_(User.name.ilike(f"%{query}%"),UserDetail.address.ilike(f"%{query}%"))).all()
    if not users:
        raise HTTPException(status_code=404,detail=f"No user with this name {query}")
    return users
