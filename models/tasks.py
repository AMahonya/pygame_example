from app.backend.database import Base
from sqlalchemy import  Text, Column, Integer, String, Boolean,  Date
from app.models import *


class Task(Base):
    __tablename__ = "task"
    __table_args__ = {"keep_existing": True}

    id = Column(Integer, primary_key=True, index=True)  # Первичный ключ, целочисленный
    name_task = Column(Text, nullable=False)
    description = Column(Text, nullable=False)  # Описание задачи, обязательно должно быть заполнено
    completed = Column(Boolean, default=False)  # Флаг завершения задачи (по умолчанию False)
    due_date = Column(Date, nullable=False)  # Крайний срок выполнения задачи
    priority = Column(String)  # Приоритет задачи (например, "high", "medium", "low")


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
