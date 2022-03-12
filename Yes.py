import requests

url = 'http://127.0.0.1:8000/account/yes/'
headers = {"X-AUTH-TOKEN":"bcb195674fa0261c646182a690c6ec71d0534392"}
response = requests.post(url,headers=headers)
print(response.status_code)
print(response.json())