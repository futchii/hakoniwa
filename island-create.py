import requests

url = 'http://127.0.0.1:8000/heiwa/create/'
headers = {"X-AUTH-TOKEN":"0a8502b0f969824921f4582e8e1f1b718f362d88"}
data = '{"name":"test_island"}'
response = requests.post(url,headers=headers,data=data)
print(response.status_code)
print(response.json())