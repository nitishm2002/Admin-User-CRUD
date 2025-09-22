from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.notification import Notification
from models.user import User


def get_message(user_id:int,db:Session):
    messages=db.query(Notification).filter(Notification.sender_id==user_id,Notification.parent_id==None).all()

    if not messages:
        raise HTTPException(status_code=404,detail="Message not Found")
    # user=db.query(User).filter(User.id==messages[0].sender_id).first()
    # if not user:
    #     raise HTTPException(status_code=404,detail="User Not Found")
    
 
   
    user_messages=[]
    for msg in messages:

        user_messages.append({
        "notification_id":msg.id,
        "user_id":msg.sender.id,
        "name":msg.sender.name,
        "email":msg.sender.email,
        "message_title":msg.title,
        "message_text":msg.message})


    return user_messages


def get_reply(user_id:int,db:Session):
    messages=db.query(Notification).filter(Notification.sender_id==user_id,Notification.parent_id!=None).all()

    if not messages:
        raise HTTPException(status_code=404,detail="Messages not found")
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    
    user_replies=[]

    for reply in messages:
        parent=db.query(Notification).filter(Notification.id==reply.parent_id).first()
        user_replies.append({
            "user_id":reply.sender.id,
            "name":reply.sender.name,
            "email":reply.sender.email,
            "query":parent.message,
            "reply":reply.message

        })

    return user_replies