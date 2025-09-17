from sqlalchemy.orm import Session
from models.cart import CartItem

def add_to_cart(db: Session, data: dict):
    item = CartItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_cart(db: Session, user_id: str):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def remove_from_cart(db: Session, item_id: str):
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
