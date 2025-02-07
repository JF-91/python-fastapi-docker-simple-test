from fastapi import APIRouter, Path, Query, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi import Path
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

templates= Jinja2Templates(directory="templates")
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully" }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

@todo_router.get("/todo/{todo_id}")
async def single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.todo_id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id:int = Path(..., title="The ID of the todo to update.")) -> dict:
    for todo in todo_list:
        if todo.todo_id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully"}
    return {"message": "Todo not found"}

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id:int = Path(..., title="The ID of the todo to delete.")) -> dict:
    for todo in todo_list:
        if todo.todo_id == todo_id:
            todo_list.remove(todo)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}


@todo_router.get("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "All todos deleted successfully"}


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {"todos": todo_list}