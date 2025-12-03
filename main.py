from sqlalchemy import insert, select, update, delete
from db import engine
from models.imperative import client_table

with engine.connect() as conn:
    # stmt = insert(client_table).values(name="Mary", email="mary@mail.com")
    # conn.execute(stmt)
    # conn.commit() -> write process

    # stmt = client_table.select().where(client_table.c.name == "John")
    # print(stmt)
    # result = conn.execute(stmt)
    # for row in result:
    #     print(row)

    # stmt = (
    #     update(client_table)
    #     .where(1 == client_table.c.id)
    #     .values(name="James", email="james@mail.com")
    # )
    # print(stmt)
    # conn.execute(stmt)
    # conn.commit()

    stmt = delete(client_table).where("Mary" == client_table.c.name)
    print(stmt)
    result = conn.execute(stmt)
    print(result.rowcount)
    conn.commit()


    