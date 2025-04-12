from sqlalchemy.orm import Session
from app.models.table import Table
from app.schemas.table import TableCreate


def get_tables(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Table).offset(skip).limit(limit).all()


def create_table(db: Session, table: TableCreate):
    # Создаем экземпляр модели Table из Pydantic-схемы
    db_table = Table(**table.model_dump())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def delete_table(db: Session, table_id: int):
    # Получаем столик по id и удаляем его
    db_table = db.query(Table).filter(Table.id == table_id).first()
    if not db_table:
        return None
    db.delete(db_table)
    db.commit()
    return db_table
