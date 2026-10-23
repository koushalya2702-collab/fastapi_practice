#post-create new food price
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FoodPrice(BaseModel):
    commodity: str
    market: str
    price: float

@app.post("/food", status_code=201)
def add_food(food: FoodPrice):
    return {
        "message": "Food price created",
        "data": food
    }

#update-the entire record
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FoodPrice(BaseModel):
    commodity: str
    market: str
    price: float

@app.put("/food",status_code=201)
def update_food(food: FoodPrice):
    return {
        "message": "Food record replaced",
        "data": food
    }


#patch-update part of a record
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FoodPriceUpdate(BaseModel):
    price: float

@app.patch("/food/{commodity}")
def update_food_price(commodity: str, food: FoodPriceUpdate):
    return {
        "message": "Food price updated",
        "commodity": commodity,
        "new_price": food.price
    }