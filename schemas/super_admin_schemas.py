from pydantic import BaseModel,EmailStr

class SendMsgUser(BaseModel):
    email:EmailStr
    title:str
    message:str

class SendReplyUser(BaseModel):
    notification_id:int
    message:str  