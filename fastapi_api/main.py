from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, select
from database import get_engine
from models import Item

app = FastAPI(title="FastAPI + SQLite Example")
engine = get_engine()


@app.on_event("startup")
def on_startup():
    # create SQLite database file and tables if they don't exist
    SQLModel.metadata.create_all(engine)


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@app.get("/items/", response_model=list[Item])
def list_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        item.name = updated.name
        item.description = updated.description
        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return {"ok": True}
