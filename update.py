import requests

url = 'http://127.0.0.1:8000/account/update/'
headers = {"X-AUTH-TOKEN":"f0ac0478742162b8f2874e055b231a1c2e76de9b"}
data = '{"name":"test","password":"pass"}'
response = requests.patch(url,headers=headers,data=data)
print(response.status_code)
print(response.json())