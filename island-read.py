import requests

url = 'http://127.0.0.1:8000/heiwa/island-read/'
headers = {"X-AUTH-TOKEN":"0a8502b0f969824921f4582e8e1f1b718f362d88"}
response = requests.get(url,headers=headers)
print(response.status_code)
print(response.json())