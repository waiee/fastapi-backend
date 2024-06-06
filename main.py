from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"Testing": "123"}

@app.post("/items")
def create_item(items:str):
    items.append(items)
    return items