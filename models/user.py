from sqlalchemy import Column,String,Integer,Boolean,DateTime,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    emp_id=Column(Integer,unique=True,nullable=False,index=True)
    name=Column(String,nullable=False,index=True)
    email=Column(String,nullable=False,unique=True,index=True)
    password=Column(String,nullable=False)
    gender=Column(String,nullable=False,index=True)
    role=Column(String,nullable=False,index=True)
    
    is_active=Column(Boolean,default=False)
    first_login=Column(Boolean,default=True)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)

    details=relationship("UserDetail",back_populates="user",uselist=False,cascade="all,delete-orphan")
    sent_notifications=relationship("Notification",back_populates="sender",foreign_keys="Notification.sender_id",cascade="all,delete-orphan")
    received_notifications=relationship("Notification",back_populates="receiver",foreign_keys="Notification.receiver_id",cascade="all,delete-orphan")
    otps=relationship("OTP",back_populates="user",cascade="all,delete-orphan")
    
