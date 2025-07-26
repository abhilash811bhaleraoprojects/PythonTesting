import requests

payload = {
    "name": "morpheus",
    "job": "leader"
}

resp = requests.post("https://reqres.in/api/users", data = payload)
print(resp)
#print(resp.json())