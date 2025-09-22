from sqlalchemy import Column,String,Integer,Boolean,DateTime,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class OTP(Base):

    __tablename__="otps"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    otp=Column(String,nullable=False)
    expires_at=Column(DateTime,nullable=False)
    created_at=Column(DateTime,nullable=False)
    is_used=Column(Boolean,default=False)

    user=relationship("User",back_populates="otps")