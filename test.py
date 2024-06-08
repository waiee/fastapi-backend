# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     text: str = None
#     is_done: bool = False

# @app.get("/")
# def root():
#     return {"Testing": "123"}

# # Global list to store items
# items_list = []
# @app.post("/items")
# def create_item(items: Item):
#     items_list.append(items)
#     return items_list

# @app.get("/items/{items_id}")
# def get_item(items_id: int) -> Item:
#     if items_id >= len(items_list) or items_id < 0:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items_list[items_id]

# # # Global list to store items
# # items_list = []
# # @app.post("/items")
# # def create_item(items: str):
# #     items_list.append(items)
# #     return items_list

# # @app.get("/items/{items_id}")
# # def get_item(items_id: int):
# #     if items_id >= len(items_list) or items_id < 0:
# #         raise HTTPException(status_code=404, detail="Item not found")
# #     return items_list[items_id]

from sqlalchemy import create_engine

# Replace 'test.db' with the full path to your database file if needed
db_url = "sqlite:///test.db"

engine = create_engine(db_url)
connection = engine.connect()

result = connection.execute("SELECT 1")
print(result.fetchone())

connection.close()
