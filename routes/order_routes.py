from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.order_crud import place_order

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/checkout/{user_id}")
def checkout(user_id: str, db: Session = Depends(get_db)):
    order = place_order(db, user_id)
    if not order:
        raise HTTPException(status_code=400, detail="Cart is empty")
    return order
