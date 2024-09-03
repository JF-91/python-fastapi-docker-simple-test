from pydantic import BaseModel
from typing import List, Optional

class Item (BaseModel):
    item: str
    status: bool    
    
class Todo(BaseModel):
    id: int
    item: Item

class TodoItem(BaseModel):
     item: str
     class Config:
         schema_extra = {
                "example": {
                    "item": "Read the next chapter of the book",
                }
            }
class TodoItems(BaseModel):
    items: List[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Read the next chapter of the book",
                    },
                    {
                        "item": "Complete the assignment",
                    }
                ]
            }
        }