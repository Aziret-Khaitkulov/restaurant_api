from pydantic import BaseModel


class TableBase(BaseModel):
    name: str
    seats: int
    location: str


# Схема для создания столика
class TableCreate(TableBase):
    pass


# Схема для обновления столика
class Table(TableBase):
    id: int

    class Config:
        from_attributes = True
