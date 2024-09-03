from fastapi import FastAPI
from todo import todo_router


app = FastAPI()

@app.get("/todos")
async def welcome() -> dict:
    return {"message": "Welcome to the Todos API!"}


app.include_router(todo_router)