from fastapi import FastAPI
from controller import ItemController
from repository.todoRepository import TodoRepository


def init_tasks():
    TodoRepository.dump_value("todo", {"items": []})


app = FastAPI()
init_tasks()

app.include_router(ItemController.router)
