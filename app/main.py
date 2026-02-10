from fastapi import FastAPI, HTTPException
from typing import List

from app.models import Task, TaskCreate, TaskUpdate
from app.crud import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task
)
from database.db import init_db

app = FastAPI(
    title="Task Manager API",
    description="Simple REST API for managing tasks",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    init_db()


@app.post("/tasks", response_model=Task)
def create(task: TaskCreate):
    return create_task(task.title, task.description)


@app.get("/tasks", response_model=List[Task])
def read_all():
    return get_tasks()


@app.get("/tasks/{task_id}", response_model=Task)
def read(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update(task_id: int, task: TaskUpdate):
    if not get_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(
        task_id,
        task.title,
        task.description,
        task.completed
    )


@app.delete("/tasks/{task_id}")
def delete(task_id: int):
    if not get_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(task_id)
    return {"message": "Task deleted"}