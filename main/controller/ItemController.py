from uuid import UUID

from fastapi import APIRouter

from model.TodoItemModel import TodoItemModel
from repository.todoRepository import TodoRepository

router = APIRouter()


@router.post("/todo_item")
def create_new_item(item: TodoItemModel):
    TodoRepository.add_item(item)


@router.get("/todo_items")
def get_all_todo():
    return TodoRepository.get_all()


@router.get("/todo_item/{id}")
def get_item_by_id(id_query: UUID) -> TodoItemModel:
    return TodoRepository.get_by_id(id_query)
