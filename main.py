from fastapi import FastAPI
from typing import Dict, Any, List

app = FastAPI()

items: List[Dict[str, Any]] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_items():
    return items

@app.post("/item")
def create_item(item: Dict[str, Any]):  # 明确指定为字典
    id = len(items) + 1
    item["id"] = id
    items.append(item)
    return item