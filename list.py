import requests

url = 'http://127.0.0.1:8000/account/list/'
headers = {"X-AUTH-TOKEN":"90b65c600619bd1df47fa8857698f4593f274e4c"}
response = requests.get(url,headers=headers)
print(response.status_code)
print(response.json())