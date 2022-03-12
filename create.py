import requests
import json

url = 'http://127.0.0.1:8000/account/create/'
data = {"name":"test1","password":"pass"}

response = requests.post(url,data=data)
print(response.status_code)
print(response.json())