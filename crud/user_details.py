
from fastapi import HTTPException
from models.user import User
from models.user_details import UserDetail
from sqlalchemy.orm import Session
from schemas.user_schemas import UserDetailsIn

def user_detail(data:UserDetailsIn,db:Session,current_user:User):

    db_user=db.query(User).filter(User.email==current_user.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="User not Found")
    user_details=db.query(UserDetail).filter(UserDetail.user_id==db_user.id).first()
    if not user_detail:
        raise HTTPException(status_code=404,detail="User Not Found")
    user_details.user_id=db_user.id
    user_details.phone=data.phone
    user_details.address=data.address
    user_details.dob=data.dob
    
    
    db.commit()
    

    return "user details entered successfully"


