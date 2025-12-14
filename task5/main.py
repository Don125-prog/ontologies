from fastapi import FastAPI
import requests
from src.config import params
import json


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello {name}"}

@app.get("/dataset_list")
def get_dataset_list():
    response = requests.get(f"http://{params['FUSEKI_HOST']}:{params['FUSEKI_PORT']}/$/datasets", auth=(params['FUSEKI_USER'], params['FUSEKI_PASSWORD']))
    if response.status_code == 200:
        return {"message": response.json()}
    else:
        return {"message": f"Ошибка при получении списка датасетов: {response.status_code}"}

@app.get("/query_test")
def query():
    with open("src/templates/template_test.rq", "r") as file:
        query = file.read()
        response = requests.post(f"http://{params['FUSEKI_HOST']}:{params['FUSEKI_PORT']}/{params['FUSEKI_DATASET']}/query", 
        auth=(params['FUSEKI_USER'], params['FUSEKI_PASSWORD']), 
        data=query.encode("utf-8"),
        headers={"Content-Type": "application/sparql-query"})


        if response.status_code == 200:
            return {"message": response.json()}
        else:
            return {"message": f"Ошибка при выполнении запроса: {response.status_code}"}
