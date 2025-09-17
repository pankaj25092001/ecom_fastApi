from sqlalchemy.orm import Session
from models.product import Product

def create_product(db: Session, product_data: dict):
    product = Product(**product_data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: str):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: str, product_data: dict):
    product = get_product(db, product_id)
    if product:
        for key, value in product_data.items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
    return product

def delete_product(db: Session, product_id: str):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product
