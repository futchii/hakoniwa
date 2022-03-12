import requests

url = 'http://127.0.0.1:8000/heiwa/create/'
headers = {"X-AUTH-TOKEN":"dd3fb9876c35d511446c3a8516c1078d01d904e7"}
data = '{"name":"test_island"}'
response = requests.post(url,headers=headers,data=data)
print(response.status_code)
print(response.json())