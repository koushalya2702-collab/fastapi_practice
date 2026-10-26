
from fastapi import FastAPI, HTTPException

app = FastAPI()

foods = [
    {"id": 1, "commodity": "Rice", "market": "Kundapura", "price": 45},
    {"id": 2, "commodity": "Wheat", "market": "Udupi", "price": 35}
]

@app.get("/food/{food_id}")
def get_food(food_id: int):
    for food in foods:
        if food["id"] == food_id:
            return food

    raise HTTPException(status_code=404, detail="Food not found")
  
    
@app.delete("/food/{food_id}")
def delete_food(food_id: int):
    for food in foods:
        if food["id"] == food_id:
            foods.remove(food)
            return {"message": "Food deleted"}
    raise HTTPException(status_code=404, detail="Food not found")


@app.get("/food")
def get_foods():
    return foods