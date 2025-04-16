from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

conn = psycopg2.connect(
    host="localhost",
    dbname="crud_demo",
    user="postgres",
    password="root"
)
cur = conn.cursor()

class Staff(BaseModel):
    name: str
    department: str

@app.get("/staff")
def read_staff():
    cur.execute("SELECT * FROM staff")
    return [{"id": row[0], "name": row[1], "department": row[2]} for row in cur.fetchall()]

@app.post("/staff")
def create_staff(staff: Staff):
    cur.execute("INSERT INTO staff (name, department) VALUES (%s, %s)", (staff.name, staff.department))
    conn.commit()
    return {"msg": "Staff added"}
