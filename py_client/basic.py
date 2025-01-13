import requests

endpoint = "http://127.0.0.1:8000/api/?abc=123"

get_response = requests.post(endpoint, json={"title": "heheh", "content": "Hello world!", "price": "234"})
print(get_response.json())
# print(get_response.headers)
# print(get_response.text)