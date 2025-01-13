import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
  "title": "Title default",
  "price": 20.00,
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
# print(get_response.headers)
# print(get_response.text)