from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status
from uuid import uuid4
from fastapi import HTTPException
from fastapi import Query


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
def ReadItems(search: str | None = Query(default=None, min_length=2, max_length=50, description="Search on word"),
            skip: int = Query(default=0, ge=0, description="How much items skip"),
            limit:int = Query(default=10, ge=1, le=50, description="Сколько задач вывести")):

    box:list = []
    if search:
        for item in items:
            if search.lower() in item["title"].lower():
                box.append(item)
        return box[skip : skip + limit]
    return items[skip : skip + limit] 


@app.get("/items/{items_id}",status_code= status.HTTP_200_OK)
def ReadItemsId(items_id:str):
    for item in items:
        if item["id"] == items_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Dont found,try another one")

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
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Dont found,try another one")   

@app.patch("/items/{items_id}")
def UpdateItems(items_id:str):
    for item in items:
        if item["id"] == items_id:
            if item["is_done"]==True:
                item["is_done"]=False
            else:
                item["is_done"]=True
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Dont found,try another one")   
        