from fastapi import FastAPI
from models import Product
app = FastAPI()
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
@app.get("/products")

def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
# If no product is found with the given ID, return a message indicating that
    return {"message": "Product not found"}



#Post request to add a new product
@app.post("/product")
#want to get product of the type Product
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"

    return "Product not found"

@app.delete("/product")
def delete_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted"
    return "Product not found"
