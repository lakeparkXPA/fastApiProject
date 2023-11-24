import requests

data = {
    "name": "test_name",
    "price": 4.99,
    "tax": 0.5
}

response = requests.put('http://127.0.0.1:8000/items/1', json=data)
print("response code: ", response.status_code)
print("response content: ", response.content)
