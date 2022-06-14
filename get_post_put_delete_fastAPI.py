from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel

class inventory(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class updateInventory(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

app = FastAPI()

@app.get("/")          #  / means homepage 
def index():
    return {"name": "First Data"}

godown = {
    1: {"brand": "Sailor",
        "product": "Shirt",
        "Price": 2677
    },

    2: {"brand": "Taaga-man",
        "product": "Punjabi",
        "Price": 4500
    }
}

#GET METHOD
#path parameter
@app.get('/get-by-id/{item_id}')
def getdata(item_id:int):
    if item_id not in inventory:
        return {'data': 'not found'}
    return inventory[item_id]
#Query parameter
@app.get('/get-by-brand-name')
def getdata(brand_name: str):
    dict = {}
    for item_id in inventory:
        if  inventory[item_id]["brand"]== brand_name:
            dict[item_id] = {"brand": inventory[item_id]["brand"], "product":inventory[item_id]["product"], "price": inventory[item_id]["price"]}
    if len(dict) == 0:
        return {"data" : "not found"}
    return dict

#POST METHOD
@app.post('/create-item')
def create_data(item: Item, item_id: int):
    if item_id in inventory:
        return "Data already exists"
    if item.brand == None or item.product == None or item.price == None:
        return "Create full details"
    inventory[item_id] = item

#PUT METHOD
@app.put('/update-item/{item_id}')
def create_item(item_id:int, item:updateInventory):
    if item_id not in godown:
        return {"Error": "Item ID doesn't exist."}
    
    if item.name != None:
        godown[item_id].name = item.name
    
    if item.price != None:
        godown[item_id].price = item.price
    
    if item.brand != None:
        godown[item_id].brand = item.brand
    return godown[item_id]

#DELETE METHOD
@app.delete('/delete-item/{item_id}')
def delete_item(item_id:int):
    if item in godown:
        del godown[item_id]
    else:
        return {'error': 'ID doesn\'t exist'}