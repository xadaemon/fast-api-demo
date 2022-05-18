import pickle
from typing import List, Dict, Any
from uuid import uuid4, UUID

from lib.datastore import datastore
from model.TodoItemModel import TodoItemModel


class TodoRepository:
    @staticmethod
    def read_value(key: str) -> Dict[str, Any]:
        val = datastore.get_key(key)
        return pickle.loads(val)

    @staticmethod
    def dump_value(key: str, value: Dict[str, Any]):
        datastore[key] = pickle.dumps(value)

    @staticmethod
    def add_item(item: TodoItemModel) -> UUID:
        item.id = uuid4()
        if len(item.body) > 1024:
            raise ValueError("Item body is too large")
        temp = TodoRepository.read_value("todo")
        temp["items"].append(item)
        TodoRepository.dump_value("todo", temp)
        return item.id

    @staticmethod
    def get_all() -> List[TodoItemModel]:
        data: List[TodoItemModel] = TodoRepository.read_value("todo")["items"]
        return data

    @staticmethod
    def get_by_id(id_query: UUID) -> TodoItemModel:
        all_items = TodoRepository.get_all()
        for item in all_items:
            if item.id == id_query:
                return item

        raise ValueError("Todo item not found")
