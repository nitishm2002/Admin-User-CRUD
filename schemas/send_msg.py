from pydantic import EmailStr,BaseModel

from typing import Optional


class SendMsg(BaseModel):
    email:EmailStr
    title:str
    message:str

class SendReply(BaseModel):
    parent_id:int
    message:str


class MessageOut(BaseModel):
    notification_id:int
    user_id: int
    name: str
    email: str
    message_title: Optional[str] = None
    message_text: str

    class Config:
        orm_mode = True


class ReplyOut(BaseModel):
    user_id: int
    name: str
    email: str
    query: str
    reply: str

    class Config:
        orm_mode = True