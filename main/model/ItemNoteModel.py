from uuid import UUID

from pydantic import BaseModel


class ItemNoteModel(BaseModel):
    id: UUID
    note: str
