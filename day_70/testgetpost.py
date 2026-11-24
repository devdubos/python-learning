from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from fastapi import status

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods = ["*"],
    allow_headers=["*"]
)   


class TaskSchema(BaseModel): 
    id: str
    title: str
    completed:bool
class TaskCreateSchema(BaseModel):
    title: str
class TaskUpdateSchema(BaseModel):
    title: str | None = None
    completed:bool | None = None

tasks:list[TaskSchema]= []



@app.get("/tasks")
def read_tasks():
    return tasks


@app.post("/tasks", status_code = status.HTTP_201_CREATED)
def create_task(payload: TaskCreateSchema):
    new_task = TaskSchema(id=str(uuid4()),title = payload.title, completed=False)
    tasks.append(new_task)
    return new_task 

@app.patch("/tasks/{task_id}")
def update_task(task_id:str, payload:TaskUpdateSchema):
    for task in tasks:
        if task.id == task_id:
            if payload.title:
                task.title = payload.title
            if payload.completed is not None:
                task.completed = payload.completed
                return task 


@app.delete("/tasks/{task_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return task
    # for i, task in enumerate(tasks):
    #     if task.id == task_id:
    #         return tasks.pop(i)



class CategoriesSchema(BaseModel):
    id: str
    name: str

class CategoriesCreateSchema(BaseModel):
    name:str

class CategoiresUpdateSchema(BaseModel):
    name:str

categories:list[CategoriesSchema] = []

@app.get("/categories")
def read_categories():
    return categories


@app.post("/categories",status_code= status.HTTP_201_CREATED)
def create_categories(payload: CategoriesCreateSchema):
    new_ctg = CategoriesSchema(id = str(uuid4()), name = payload.name)
    categories.append(new_ctg)
    return new_ctg

@app.patch("/categories/{ctg_id}")
def update_categories(ctg_id:str, payload:CategoiresUpdateSchema):
    for ctg in categories:
        if ctg.id == ctg_id:
            if payload.name:
                ctg.name = payload.name
                return ctg

@app.delete("/categories/{ctg_id}")
def delete_categories(ctg_id:str,):
    for ctg in categories:
        if ctg.id == ctg_id:
            categories.remove(ctg)
            return categories