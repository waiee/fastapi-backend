from fastapi import FastAPI, HTTPException

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

@app.get("/items/{items_id}")
def get_item(items_id: int):
    if items_id >= len(items_list) or items_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_list[items_id]
