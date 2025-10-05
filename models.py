from pydantic import BaseModel
# BaseModel is used to create data models with type validation and serialization capabilities.

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    quantity: int

    #below is not needed as Pydantic's BaseModel automatically handles initialization

    # def __init__(self, id: int, name: str, description: str, price: int, quantity: int):
    #     self.id = id
    #     self.name = name 
    #     self.description  = description
    #     self.price = price
    #     self.quantity = quantity