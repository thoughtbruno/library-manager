from pydantic import BaseModel
from typing import Optional


class DocumentBase(BaseModel):
    title: str
    type: str
    extension: str


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    type: Optional[str] = None
    extension: Optional[str] = None


class DocumentResponse(DocumentBase):
    id: int

    class Config:
        from_attributes = True 