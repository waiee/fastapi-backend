from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Testing": "123"}

# Global list to store items
items_list = []

@app.post("/items")
def create_item(items: str):
    items_list.append(items)
    return items_list
