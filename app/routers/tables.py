from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.table import TableCreate, Table as TableSchema
from app.services.tables import get_tables, create_table, delete_table
from app.database import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/tables/", response_model=list[TableSchema])
def read_tables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Получаем все таблицы из базы данных
    tables = get_tables(db, skip=skip, limit=limit)
    return tables


@router.post("/tables/", response_model=TableSchema)
def add_table(table: TableCreate, db: Session = Depends(get_db)):
    # Создаем новый чтоклик
    new_table = create_table(db, table)
    return new_table


@router.delete("/tables/{table_id}", response_model=TableSchema)
def remove_table(table_id: int, db: Session = Depends(get_db)):
    # Удаляем столик по ID
    db_table = delete_table(db, table_id)
    if db_table is None:
        raise HTTPException(status_code=404, detail="Столик не найден")
    return db_table 
