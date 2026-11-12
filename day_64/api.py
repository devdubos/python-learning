from fastapi import FastAPI
from pydantic import BaseModel

# app = FastAPI(title="My First API")


# class Task(BaseModel):
#     title: str
#     is_done: bool = False


# tasks_db = [
#     {"id": 1, "title": "Learn Python basics", "is_done": True},
#     {"id": 2, "title": "Run first FastAPI server", "is_done": False},
# ]


# @app.get("/")
# def read_root():
#     return {"message": "Hello! My first FastAPI server is running!"}


# @app.get("/tasks")
# def get_tasks():
#     return tasks_db


# @app.post("/tasks")
# def create_task(task: Task):
#     new_task = {
#         "id": len(tasks_db) + 1,
#         "title": task.title,
#         "is_done": task.is_done,
#     }
#     tasks_db.append(new_task)
#     return {"status": "Task created", "task": new_task}





import asyncio
import random

app = FastAPI()

@app.get("/")
async def slow_hello():
    delay = round(random.uniform(1, 3), 2)
    await asyncio.sleep(delay)
    return {"message": "Привет!", "slept_seconds": delay}