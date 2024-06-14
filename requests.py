import requests
import json

link = "https://fatec-pi-5-default-rtdb.firebaseio.com/"

def SaveData(values):
    data = json.dumps(values)
    req = requests.post(f"{link}/Resultado/.json", data=data)
