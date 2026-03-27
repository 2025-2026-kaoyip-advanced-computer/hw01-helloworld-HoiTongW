import sqlite3
from fastapi import FastAPI
from typing import Dict, Any, List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/submit")
    def submit_form(data: Dict[str, Any]):
        print(data)
        return {"message": "Form submitted successfully", "data": data}

@app.post('/register')
def register_user(data: Dict[str, Any]):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO students (name, student_id, class) VALUES (?, ?, ?)",
                (data.get("name"), data.get("password"), "Class A"))
    con.commit()
    con.close()
    return {"message": "User registered successfully", "data": data}

@app.get("/testing")
def testing():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * from students;")
    return cur.fetchall()


conn = sqlite3.connect('database.db')
conn.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
conn.commit()




items: List[Dict[str, Any]] = [
    {"id": 1, "Name": "laisir"},
    {"id": 2, "Name": "laisir_iphone"},
    {"id": 3, "Name": "laisir_laptop"},
    {"id": 4, "Name": "laisir_tablette"}
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_items():
    return items

@app.post("/item")
def create_item(item: Dict[str, Any]):
    id = len(items) + 1
    item["id"] = id
    items.append(item)
    return item

@app.delete("/{itemID}")
def delete_item(itemID: str):
    global items
    items = [item for item in items if item["id"] != int(itemID)]
    return {"message": "Item deleted successfully"}

@app.post("/register")
def register_user(data: Dict[str, Any]):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    sql = "INSERT INTO users_table (UserN, PWhash) VALUES (?, ?)"
    cur.execute(sql, (data.get("username"), data.get("password_hash")))
    con.commit()
    con.close()
    return {"message": "User registered successfully", "data": data}
