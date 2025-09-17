from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database and models
from database import Base, engine

# Import routers
from routes.product_routes import router as product_router
from routes.cart_routes import router as cart_router
from routes.order_routes import router as order_router
from routes.auth_routes import router as auth_router  # ✅ JWT auth routes

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="E-Commerce Backend with Auth & Cart")

# CORS setup (allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(product_router, prefix="/api", tags=["Products"])
app.include_router(cart_router, prefix="/api", tags=["Cart"])
app.include_router(order_router, prefix="/api", tags=["Orders"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])  # ✅

# Root route
@app.get("/")
def root():
    return {"message": "Backend is live with JWT Auth, Cart, Orders, and Products!"}
