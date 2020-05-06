import requests
import json

data = requests.get("https://api.github.com/users")
print(type(data.text))
data_json = data.json()
print(type(data_json))

print(data_json[2])

# data = requests.get("https://api.exchangeratesapi.io/2000-01-03")
# print(type(data.text))
# data_json = data.json()
# print(data_json)
# print(data_json['rates']["PLN"])