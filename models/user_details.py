from sqlalchemy import Column,String,Integer,Boolean,Date,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class UserDetail(Base):
    __tablename__="user_details"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),index=True,nullable=False)
    phone=Column(String,nullable=True,unique=True,index=True)
    address=Column(String,nullable=True,index=True)
    dob=Column(Date,nullable=True,index=True)

    user=relationship("User",back_populates="details")