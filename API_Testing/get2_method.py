import requests

json = requests.get("https://reqres.in/api/users/2")
print(json.status_code)
assert json.status_code == 200 ,"code not matching"