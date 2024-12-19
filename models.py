from fastapi import FastAPI
from pydantic import BaseModel


# Pydantic model for a Todo item
class Todo(BaseModel):
    id: int
    item: str