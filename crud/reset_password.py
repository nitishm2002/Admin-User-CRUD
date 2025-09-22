from fastapi import HTTPException,Depends,status
from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schemas import ChangePassword,ForgotPassword,VerifyOTP
from core.security import Hash
import random
from utils.send_email import send_otp_email
from models.otps import OTP
from db.database import get_db
from datetime import datetime,timedelta
from core.create_token import create_access_token,verify_token


credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
def generate_otp():
    otp=random.randint(1000,9999)
    return otp

def forgot_password(data:ForgotPassword,db:Session):
    db_user=db.query(User).filter(User.email==data.email).first()
    if not db_user:
        raise HTTPException(status_code=404 ,detail="Email Not Found")
    otp=generate_otp()
    send_otp_email(data.email,otp)
    otp_create_time=datetime.utcnow()
    otp_expiry_time=otp_create_time+timedelta(minutes=5)
    user_otp=OTP(user_id=db_user.id,otp=otp,expires_at=otp_expiry_time,created_at=otp_create_time)
    db.add(user_otp)
    db.commit()
    db.refresh(user_otp)

    return "OTP send Successfully"


def verify_otp(data:VerifyOTP,db:Session):
    db_user=db.query(User).filter(User.email==data.email).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="Email not Found")
    user_otp=db.query(OTP).filter(OTP.user_id==db_user.id).order_by(OTP.created_at.desc()).first()
    if not user_otp:
        raise HTTPException(status_code=404,detail="otp not found")
    if user_otp.is_used==True:
        raise HTTPException(status_code=401,detail="otp is already used")
    if data.otp!=user_otp.otp:
        raise HTTPException(status_code=403,detail="otp did not match")
    if user_otp.expires_at < datetime.utcnow():
        raise HTTPException(status_code=403,detail="OTP expires")
    
    user_otp.is_used=True
    db.commit()

    access_token=create_access_token(data={"sub":data.email,"role":"user"})

    return access_token
    

def reset_password(token:str,data:ChangePassword,db:Session):
    user=verify_token(token,credentials_exception,db)
    if not user:
        return "some thing is haapends"
    print("hellooo")
    db_user=db.query(User).filter(User.email==user.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="user Not Found")
    if data.new_password!=data.confirm_password:
        raise HTTPException(status_code=403,detail="passowrd and confirm passowrd should be same.")

    db_user.password=Hash.hash_password(data.new_password)
    db_user.first_login=False
    db.commit()
    
    return "password changed successfully"
    


    

    
    

