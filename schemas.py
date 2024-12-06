from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List
from datetime import datetime, date
from uuid import UUID
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.backend.database import sessionmaker




# Модель для валидации данных задачи при создании
class TaskCreate(BaseModel):
    name_task: str = Field(..., min_length=3, max_length=18)
    description: str = Field(..., min_length=3, max_length=255) #Описание задачи, не менее 3, не более 255 символов
    due_date: date = Field(..., example="2024-03-15T10:30:00") #Крайний срок задачи
    priority: str = Field("medium", example="high") #Приоритет задачи
    completed: bool = False




# Модель для валидации данных задачи при обновлении
class TaskUpdate(BaseModel):
    name_task: Optional[str] = None #Имя задачи, необязательное поле
    description: Optional[str] = None #Описание задачи, необязательное поле
    due_date: Optional[datetime] = None #Крайний срок задачи, необязательное поле
    completed: Optional[bool] = None #флаг завершения задачи
    priority: Optional[str] = None #Приоритет задачи, необязательное поле

    @field_validator('priority')
    def check_priority(cls, v):
        allowed_priorities = ["high", "medium", "low"]
        if v not in allowed_priorities:
            raise ValueError("Priority must be one of: high, medium, low")
        return v


# Модель для представления данных задачи
class Task(BaseModel):
    id: int
    name_task: str
    description: str
    completed: bool
    due_date: datetime
    priority: str
    user_id: int
    created_at: datetime
    updated_at: datetime
    # user: User  # Включили модель пользователя для удобства представления

    class Config:
        from_attributes = True


# Модель для JWT токена
