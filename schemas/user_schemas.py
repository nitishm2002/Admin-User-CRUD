from pydantic import BaseModel,EmailStr,validator
from typing import Optional
from datetime import date,datetime

class UserIn(BaseModel):
    name:str
    email:EmailStr
    gender:str
    
    @validator("name")
    def validate_name(cls,value):
        if not value.strip():
            raise ValueError("Name can not be Empty")
        if value.isdigit():
            raise ValueError("Name can not be only number")
        return value

class UserDetailsOut(BaseModel):
    phone:Optional[int]=None
    address:Optional[str]=None
    dob:Optional[date]=None


    class Config:
        orm_mode=True

class UserDetailsIn(UserDetailsOut):
    pass

class UserOut(BaseModel):
    id:int
    name:str
    email:EmailStr
    gender:str
    role:str
    is_active:bool
    created_at:datetime
    updated_at:datetime
    details:Optional[UserDetailsOut]

    class Config:
        orm_mode=True


class UserLogin(BaseModel):
    email:EmailStr
    password:str

class ChangePassword(BaseModel):
    email:EmailStr
    new_password:str
    confirm_password:str

class ForgotPassword(BaseModel):
    email:EmailStr

class ResetPassword(BaseModel):
    email:EmailStr
    new_password:str
    confirm_password:str

class VerifyOTP(BaseModel):
    email:EmailStr
    otp:str
    
class SendReplyAdmin(BaseModel):
    notification_id:int
    message:str    
class SendMsgAdmin(BaseModel):
    email:EmailStr
    title:str
    message:str
