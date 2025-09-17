from sqlalchemy.orm import Session
from database import SessionLocal
from models.product import Product
from models.user import User
from auth.utils import hash_password

def seed_products(db: Session):
    products = [
        Product(
            name="Nike Air Max",
            description="Comfortable running shoes",
            price=7999,
            stock=50,
            image_url="https://example.com/nike.jpg"
        ),
        Product(
            name="Adidas Ultraboost",
            description="High-performance sports shoes",
            price=8999,
            stock=40,
            image_url="https://example.com/adidas.jpg"
        ),
        Product(
            name="Puma Sneakers",
            description="Stylish everyday sneakers",
            price=4999,
            stock=60,
            image_url="https://example.com/puma.jpg"
        ),
        Product(
            name="Apple Watch Series 8",
            description="Smartwatch with health tracking",
            price=29999,
            stock=30,
            image_url="https://example.com/applewatch.jpg"
        ),
        Product(
            name="Samsung Galaxy Buds",
            description="Wireless earbuds with noise cancellation",
            price=5999,
            stock=70,
            image_url="https://example.com/galaxybuds.jpg"
        ),
    ]
    db.add_all(products)
    db.commit()
    print("✅ Products seeded")

def seed_users(db: Session):
    users = [
        User(
            email="test1@example.com",
            password=hash_password("pass123")
        ),
        User(
            email="test2@example.com",
            password=hash_password("pass456")
        ),
    ]
    db.add_all(users)
    db.commit()
    print("✅ Users seeded")

def run():
    db = SessionLocal()
    seed_products(db)
    seed_users(db)
    db.close()
    print("🎉 All dummy data inserted successfully")

if __name__ == "__main__":
    run()
