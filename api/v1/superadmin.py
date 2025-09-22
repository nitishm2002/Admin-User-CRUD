from fastapi import Depends,HTTPException,FastAPI,APIRouter,WebSocket,WebSocketDisconnect
from sqlalchemy.orm import Session
from schemas.user_schemas import UserIn,UserOut
from schemas.super_admin_schemas import SendMsgUser,SendReplyUser
from schemas.send_msg import MessageOut,ReplyOut,SendMsg,SendReply
from db.database import get_db
from crud.create_user import create_user
from crud.get_user import get_user
from crud.get_all_users import get_all_users
from crud.send_msg import send_msg
from crud.send_reply import send_reply
from crud.get_message import get_message,get_reply
from crud.filter_user import filter_user
from models.user import User
from core.oauth2 import get_current_admin
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from crud.login_superadmin import login_superadmin
from crud.delete_user import delete_user
# from core.ws_manager import manager


router=APIRouter()

@router.post("/add-user")
def add_user(data:UserIn,db:Session=Depends(get_db),current_admin:User=Depends(get_current_admin)):
    return create_user(data,db,current_admin)

@router.get("/get-user/{user_id}",response_model=UserOut)
def fetch_user(user_id:int,db:Session=Depends(get_db)):
    return get_user(user_id,db)

@router.get("/get-all-user",response_model=List[UserOut])
def get_all_user(db:Session=Depends(get_db)):
    return get_all_users(db)

@router.post("/send-message-touser")
def send_msg_touser(data:SendMsg,db:Session=Depends(get_db),current_admin:User=Depends(get_current_admin)):
    return send_msg(data,db,current_admin)

@router.post("/send-reply-touser")
def send_reply_touser(data:SendReply,db:Session=Depends(get_db),current_admin:User=Depends(get_current_admin)):
    return send_reply(data,db,current_admin)

@router.get("/get-user-msg/{user_id}")
def get_user_msg(user_id:int,db:Session=Depends(get_db)):
    return get_message(user_id,db)

@router.get("/get-user-reply/{user_id}")
def get_user_replies(user_id:int,db:Session=Depends(get_db)):
    return get_reply(user_id,db)

@router.get("/filter-user",response_model=List[UserOut])
def filter_users(query:str,db:Session=Depends(get_db)):
    return filter_user(query,db)

@router.post("/login")
def user_superadmin(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return login_superadmin(data,db)


@router.delete("/delete-user/{user_id}")
def user_delete(user_id:int,db:Session=Depends(get_db)):
    return delete_user(user_id,db)




