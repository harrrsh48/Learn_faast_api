from fastapi import FastAPI
import json

def load_data():
    with open("database","r") as f:
        return json.load(f)

app=FastAPI()




@app.get("/")
def hello():
    return {"messaage":"Hello peopleihjn8uhj9"}

@app.get("/view")
def view_data():
    data = load_data()
    return {"data": data}