from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the data structure for an item using Pydantic
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}") # Defines a PUT endpoint to update an item using its ID in the URL
def update_item(item_id: int, item: Item): # Accepts the item ID as an integer path parameter
    # Accepts the request body as an Item object, validated using the Pydantic model
    return {"item_name": item.name, "item_id": item_id} # Returns a dictionary containing the item's name and ID as JSON
