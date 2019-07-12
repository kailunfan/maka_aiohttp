import requests

data = {"phone": "13526532589"}
res = requests.post("http://127.0.0.1:8080/user/login", data=data)
print(res.json())

token = res.json()['token']
res = requests.get("http://127.0.0.1:8080/user", headers={"token": token})
print(res.content.decode())
