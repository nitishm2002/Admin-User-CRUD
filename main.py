from fastapi import FastAPI,Depends,APIRouter
from contextlib import asynccontextmanager
from db.database import get_db,Base,engine,SessionLocal
from sqlalchemy.orm import Session
from core.security import Hash
from models.user import User

from datetime import datetime
from api.v1.superadmin import router as superadmin
from api.v1.user_routes import router as user_routes

Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.on_event("startup")
def create_super_admin():
    db=SessionLocal()
    try:
        super_admin=db.query(User).filter(User.email=="dhruvpatel2581@gmail.com").first()
        if not super_admin:
            last_emp=db.query(User).order_by(User.emp_id.desc()).first()
            new_admin=User(
                emp_id=last_emp.emp_id+1 if last_emp else 1,
                name="Super Admin",
                email="dhruvpatel2581@gmail.com",
                password=Hash.hash_password("superadmin123"),
                gender="male",
                role="superadmin",
                is_active=True,
                first_login=False,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.add(new_admin)
            db.commit()
            db.refresh(new_admin)
            

            print("super admin created")
        else:
            print("super admin already exists")
        
    finally:
        db.close()



app.include_router(superadmin,prefix="/api/v1/superadmin",tags=["Super Admin"])
app.include_router(user_routes,prefix="/api/v1",tags=["Users"])

