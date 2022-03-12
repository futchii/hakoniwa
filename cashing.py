import requests

url = 'http://127.0.0.1:8000/heiwa/cashing/'
headers = {"X-AUTH-TOKEN":"dd3fb9876c35d511446c3a8516c1078d01d904e7"}
response = requests.get(url,headers=headers)
print(response.status_code)
print(response.json())