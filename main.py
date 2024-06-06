from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return("Cubaan 1 2 3 testing bismillah")