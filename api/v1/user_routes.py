from fastapi import Depends,HTTPException,FastAPI,APIRouter
from sqlalchemy.orm import Session
from schemas.user_schemas import UserIn
from schemas.send_msg import MessageOut,ReplyOut,SendMsg,SendReply
from db.database import get_db
from crud.create_user import create_user
from schemas.user_schemas import UserLogin
from crud.login_user import login_user
from schemas.user_schemas import ChangePassword,ResetPassword,VerifyOTP,ForgotPassword,UserDetailsIn,SendReplyAdmin,SendMsgAdmin
from models.user import User
from core.oauth2 import get_current_user
from crud.change_password import change_password
from crud.reset_password import forgot_password,reset_password,verify_otp
from crud.user_details import user_detail
from crud.send_reply import send_reply
from crud.send_msg import send_msg
from crud.get_message import get_message,get_reply
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter()

@router.post("/login")
def user_login(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return login_user(data,db)

@router.post("/change-password")
def password_change(data:ChangePassword,db:Session=Depends(get_db),get_current_user:User=Depends(get_current_user)):
    return change_password(data,db,get_current_user)

@router.post("/forgot-password")
def password_forgot(data:ForgotPassword,db:Session=Depends(get_db)):
    return forgot_password(data,db)

    
@router.post("/verify-otp")
def otp_verify(data:VerifyOTP,db:Session=Depends(get_db)):
    return verify_otp(data,db)
    

@router.post("/reset-password")
def password_reset(token:str,data:ResetPassword,db:Session=Depends(get_db),):
    return reset_password(token,data,db)


@router.put("/user-detail")
def enter_user_detail(data:UserDetailsIn,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return user_detail(data,db,current_user)

@router.post("/send-reply-to-admin")
def send_reply_toadmin(data:SendReply,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return send_reply(data,db,current_user)

@router.post("/send-message-toadmin")
def send_msg_toadmin(data:SendMsg,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return send_msg(data,db,current_user)

@router.get("/get-admin-message/{user_id}")
def get_messages(user_id:int,db:Session=Depends(get_db)):
    return get_message(user_id,db)

@router.get("/get-admin-reply/{user_id}")
def get_replies(user_id:int,db:Session=Depends(get_db)):
    return get_reply(user_id,db)