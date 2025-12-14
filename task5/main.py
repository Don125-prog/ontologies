from fastapi import FastAPI
import requests
from src.config import params


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
