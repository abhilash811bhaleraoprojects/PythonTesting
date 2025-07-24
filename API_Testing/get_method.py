import requests

response = requests.get("https://reqres.in/api/users?page=2")
print(response)
print(type(response))
print(dir(response))