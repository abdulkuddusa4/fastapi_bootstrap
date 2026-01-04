from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, inspect, text
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.sql.sqltypes import Integer, Float, String
import sys
import pkgutil

sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite+aiosqlite:///{sqlite_file_name}"  # Changed to async driver

engine = create_async_engine(sqlite_url, echo=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

print(*list(pkgutil.iter_modules([__package__])), sep='\n')
print("abc", pkgutil.get_loader("/home/roni/Documents/adigarson_bakend/booking_app"))

def load_models():
    for item in pkgutil.iter_modules([__package__]):
        if item.ispkg:
            for inner_item in pkgutil.iter_modules([item.name]):
                if inner_item.name == 'models':
                    __import__(f"{item.name}.{inner_item.name}")

def map_column_type(column_type):
    """Map SQLAlchemy types to SQLite types for ALTER TABLE."""
    if isinstance(column_type, Integer):
        return "INTEGER"
    elif isinstance(column_type, Float):
        return "REAL"
    else:
        return "TEXT"

async def run_auto_migrations():
    load_models()
    
    async with engine.connect() as conn:
        # Use run_sync for inspect since it's not async
        inspector = await conn.run_sync(lambda sync_conn: inspect(sync_conn))
        existing_tables = await conn.run_sync(lambda sync_conn: inspect(sync_conn).get_table_names())
        
        for table_name, table in SQLModel.metadata.tables.items():
            # If table doesn't exist → create it
            if table_name not in existing_tables:
                await conn.run_sync(SQLModel.metadata.create_all)
                continue
            
            # Table exists → check columns
            existing_columns = [
                col["name"] 
                for col in await conn.run_sync(
                    lambda sync_conn: inspect(sync_conn).get_columns(table_name)
                )
            ]
            
            for column in table.columns:
                column_name = column.name
                if column_name not in existing_columns:
                    sql_type = map_column_type(column.type)
                    await conn.execute(
                        text(f'ALTER TABLE {table_name} ADD COLUMN {column_name} {sql_type}')
                    )
                    await conn.commit()
                    print(f"Added column {column_name} to table {table_name}")


async def create_db_and_tables():
    load_models()
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async with async_session_maker() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]