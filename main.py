from database import session,engine
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
import database_models
from sqlalchemy.orm import Session



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return "Hello, World!"
# as of now, we are using in-memory storage for products BaseModel we can define the structure of our product data
products = [
    Product(id=1, name="Mobile", description="Budget Phone", price=99, quantity=10),
    Product(id=2, name="Laptop", description="gaming laptop", price=999, quantity=3),
    Product(id=9, name="Headphones", description="Noise Cancelling", price=199, quantity=15),
    Product(id=6, name="Monitor", description="4K UHD", price=399, quantity=7)
]

 
# products = [
#     Product(1, "Mobile", "Budget Phone", 99, 10),
#     Product(2, "Laptop", "gameing laptop", 999, 3)
# ]

def get_db():
    db = session()
    try: 
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()

@app.get("/products")

def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"
# If no product is found with the given ID, return a message indicating that
    return {"message": "Product not found"}



#Post request to add a new product
@app.post("/products")
#want to get product of the type Product
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated"
    else:
        return "Product not found"

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    else:
        return "Product not found"
