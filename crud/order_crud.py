from sqlalchemy.orm import Session
from models.order import Order
from models.cart import CartItem

def place_order(db: Session, user_id: str):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    if not cart_items:
        return None

    total = sum(item.quantity * 100 for item in cart_items)  # Replace 100 with actual product price lookup

    order = Order(user_id=user_id, total_amount=total)
    db.add(order)
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()
    db.refresh(order)
    return order
