# SqlAlchemy Core

# metadata -> object in SQLAlchemy Core acts as a central registry or container for all the schema definitions
# (tables, columns, constraints) that you are modeling in your application.

from sqlalchemy import MetaData, Table, Column, String, Integer

from db import engine

metadata = MetaData()

client_table: Table = Table(
    "client",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String(100), nullable=False),
)

metadata.create_all(engine)

