import requests
import json

URL = "http://localhost:11434/api/generate"

payload = {
    "model": "evilceo",   
    "prompt": "Can i wear business casuals",
    "stream": False
}

response = requests.post(URL, json=payload)

print(response.json()['response'])
