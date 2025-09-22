from sqlalchemy import Column,String,Integer,Boolean,DateTime,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class Notification(Base):
    __tablename__="notifications"

    id=Column(Integer,primary_key=True,index=True)
    sender_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),index=True,nullable=False)
    receiver_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),index=True,nullable=False)
    parent_id=Column(Integer,ForeignKey("notifications.id",ondelete="CASCADE"),index=True,nullable=True)
    title=Column(String,nullable=True,index=True)
    message=Column(String,nullable=True,index=True)
    is_read=Column(Boolean,default=False)
    created_at=Column(DateTime)

    sender=relationship("User",foreign_keys=[sender_id],back_populates="sent_notifications")
    receiver=relationship("User",foreign_keys=[receiver_id],back_populates="received_notifications")