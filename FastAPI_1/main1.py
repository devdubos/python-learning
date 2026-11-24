from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status
from uuid import uuid4

app = FastAPI()

items = [
    {"id": "1", "title": "Купить молоко","is_done": False},
    {"id": "2", "title": "Разобраться with Swagger","is_done": False},
    {"id": "3", "title": "Написать POST-запрос","is_done": True},
]


class ItemSchema(BaseModel):
    id: str
    title: str
    is_done: bool


class ItemsCreateSchema(BaseModel):
    title: str
    is_done: bool

@app.get("/items",status_code= status.HTTP_200_OK)
def ReadItems(search: str | None = None):
    box:list = []
    if search:
        for item in items:
            if search.lower() in item["title"].lower():
                box.append(item)
        return box
    return items 


@app.get("/items/{items_id}",status_code= status.HTTP_200_OK)
def ReadItemsId(items_id:str):
    for item in items:
        if item["id"] == items_id:
            return item

@app.post("/items", status_code=status.HTTP_201_CREATED   )        
def CreateItems (payload:ItemsCreateSchema):
    new_item = ItemSchema(id = str(uuid4()), title= payload.title,is_done= False)
    items.append(new_item.model_dump())
    return items


@app.delete("/items/{items_id}",status_code=status.HTTP_204_NO_CONTENT  )   
def DeleteItemId(items_id:str):
    for item in items:
        if item["id"] == items_id:
            items.remove(item)
    return items

@app.patch("/items/{items_id}")
def UpdateItems(items_id:str):
    for item in items:
        if item["id"] == items_id:
            if item["is_done"]==True:
                item["is_done"]=False
            else:
                item["is_done"]=True
            return item
        if not item:
            return items