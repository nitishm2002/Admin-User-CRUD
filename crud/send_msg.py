from sqlalchemy.orm import Session
from schemas.user_schemas import SendMsgAdmin
from schemas.send_msg import SendMsg
from models.user import User
from models.notification import Notification
from fastapi import HTTPException
from datetime import datetime
from utils.send_email import send_notify_email
# def send_msg_to_admin(data:SendMsgAdmin,db:Session,current_user:User):
#     db_user=db.query(User).filter(User.email==data.email).first()

#     if not db_user:
#         raise HTTPException(status_code=404,detail="Admin  Not Found")
#     msg=Notification(sender_id=current_user.id,receiver_id=db_user.id,parent_id=None,title=data.title,message=data.message,created_at=datetime.now())
#     db.add(msg)
#     db.commit()
#     db.refresh(msg)

#     return "message sent successfully to admin"
# def send_msg_to_user(data:SendMsgUser,db:Session):
#     db_user=db.query(User).filter(User.email==data.email).first()

#     if not db_user:
#         raise HTTPException(status_code=404,detail="User Not Found")
#     msg=Notification(sender_id=1,receiver_id=db_user.id,parent_id=None,title=data.title,message=data.message,created_at=datetime.now())
#     db.add(msg)
#     db.commit()
#     db.refresh(msg)

#     return "message sent successfully to user"


def send_msg(data:SendMsg,db:Session,current_user:User=None):
    db_user=db.query(User).filter(User.email==data.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="User Not Found")
    msg=None
    if db_user.role=="superadmin":
        print(current_user.id)
        msg=Notification(sender_id=current_user.id,receiver_id=db_user.id,parent_id=None,title=data.title,message=data.message,created_at=datetime.now())
    if db_user.role=="user":
        send_notify_email(data.email)
        print(current_user.id)
        msg=Notification(sender_id=current_user.id,receiver_id=db_user.id,parent_id=None,title=data.title,message=data.message,created_at=datetime.now())

    
    db.add(msg)
    db.commit()
    db.refresh(msg)

    return "message sent successfully."