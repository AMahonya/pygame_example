from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, UploadFile, File, Request, Form
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from app.backend.db_depends import get_db
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, Task

from datetime import datetime
import sys
import os
from pydantic import ValidationError

sys.path.append('..')

router = APIRouter(
    prefix="/tasks",
    tags=['Диспетчер задачь'],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': 'Not found'
        }
    }
)

templates = Jinja2Templates(directory='templates')


@router.get("/tasks")
async def read_tasks(request: Request):
    tasks = db.query(Task).all()
    db.close()
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})

@router.post("/tasks")
async def create_task(name_task: str = Form(...), description: str = Form(...), due_date: str = Form(...), priority: str = Form(...)):
    task = Task(name_task=name_task, description=description, due_date=due_date, priority=priority)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return RedirectResponse(url="/tasks", status_code=303)



@router.get("/tasks/{task_id}")
async def read_task(request: Request, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    return templates.TemplateResponse("task.html", {"request": request, "task": task})

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, completed: bool = Form(...)):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.completed = completed
    db.commit()
    db.close()
    return RedirectResponse(url=f"/tasks/{task_id}", status_code=303)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)
    db.commit()
    db.close()
    return RedirectResponse(url="/tasks", status_code=303)
