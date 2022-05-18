import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from model.ItemNoteModel import ItemNoteModel


class TodoItemModel(BaseModel):
    id: UUID
    name: str
    body: str
    is_done: bool
    due_date: datetime.date
    notes: List[ItemNoteModel]
