import requests

endpoint = "http://127.0.0.1:8000/api/products/837923759832/"

get_response = requests.get(endpoint)
print(get_response.json())
# print(get_response.headers)
# print(get_response.text)