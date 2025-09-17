from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud.cart_crud import *
from pydantic import BaseModel

router = APIRouter()

class CartSchema(BaseModel):
    user_id: str
    product_id: str
    quantity: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cart")
def add_item(item: CartSchema, db: Session = Depends(get_db)):
    return add_to_cart(db, item.dict())

@router.get("/cart/{user_id}")
def view_cart(user_id: str, db: Session = Depends(get_db)):
    return get_cart(db, user_id)

@router.delete("/cart/{item_id}")
def delete_item(item_id: str, db: Session = Depends(get_db)):
    return remove_from_cart(db, item_id)
