import json

import requests

url = "http://127.0.0.1:8000/api/chatgpt/chat-stream"
message = "What's the company name and What time does company working?"
data = {"query": message}

headers = {"Content-type": "application/json"}

with requests.post(url, data=json.dumps(data), headers=headers, stream=True) as r:
    for chunk in r.iter_content(1024):
        print(chunk)