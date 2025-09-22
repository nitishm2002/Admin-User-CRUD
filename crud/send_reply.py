from sqlalchemy.orm import Session
from schemas.send_msg import SendReply
from models.user import User
from models.notification import Notification
from fastapi import HTTPException
from datetime import datetime
from utils.send_email import send_notify_email

def send_reply(data:SendReply,db:Session,current_user:User=None):
    parent_msg=db.query(Notification).filter(Notification.id==data.parent_id).first()

    if not parent_msg:
        raise HTTPException(status_code=404,detail="Msg Not Found")
    user=db.query(User).filter(User.id==parent_msg.sender_id).first()
    reply=None
    print(f"the role is{user.role}")
    if user.role=="user":
        reply=Notification(sender_id=current_user.id,receiver_id=parent_msg.sender_id,parent_id=parent_msg.id,title=parent_msg.message,message=data.message,created_at=datetime.now())
        send_notify_email(user.email)
    elif user.role=="superadmin":
        reply=Notification(sender_id=current_user.id,receiver_id=parent_msg.sender_id,parent_id=parent_msg.id,title=parent_msg.message,message=data.message,created_at=datetime.now())


    db.add(reply)
    db.commit()
    db.refresh(reply)

    return "reply send successfully"

