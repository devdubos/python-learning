from fastapi import FastAPI
import asyncio
import random
from pydantic import BaseModel

app = FastAPI(title="My FastAPI Learning")

class Note(BaseModel):
    title: str
    content: str
    is_urgent: bool = False

@app.get("/")
async def root():
    delay = round(random.uniform(0.5, 2.0), 2)
    await asyncio.sleep(delay)
    return {"status": "ok", "simulated_delay": delay}

@app.get("/items/{item_id}")
async def get_item(item_id: int, discount: bool = False):
    price = 100
    if discount:
        price = 80
    return {
        "item_id": item_id,
        "discount_applied": discount,
        "final_price": price
    }

@app.post("/notes")
async def create_note(note: Note):
    return {
        "message": "Заметка успешно создана",
        "data": note
    }