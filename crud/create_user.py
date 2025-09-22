from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user_schemas import UserIn
from models.user import User
from models.user_details import UserDetail
from core.security import Hash,generate_password
from datetime import datetime
from utils.send_email import send_notification_email


def create_user(data:UserIn,db:Session,current_admin:User):
    db_user=db.query(User).filter(User.email==data.email).first()
    if db_user:
        raise HTTPException(status_code=404,detail="Email Already Registered")
    plain_password=generate_password()
    hashed_password=Hash.hash_password(plain_password)
    last_emp=db.query(User).order_by(User.emp_id.desc()).first()
    emp_id=last_emp.emp_id+1 if last_emp else 1
    new_user=User(emp_id=emp_id,name=data.name,email=data.email,password=hashed_password,gender=data.gender,role="user",is_active=True,first_login=True,created_at=datetime.now(),updated_at=datetime.now())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    user_details=UserDetail(user_id=new_user.id,phone=None,address=None,dob=None)

    db.add(user_details)
    db.commit()
    db.refresh(user_details)

    send_notification_email(data.email,data.name,plain_password)

    return {"new user created"}