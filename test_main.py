import requests

data = {
    "name": "test_name",
    "price": 4.99,
}

response = requests.post('http://127.0.0.1:8000/items/', json=data)
print("response code: ", response.status_code)
print("response content: ", response.content)
