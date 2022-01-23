import requests

BASE = 'http://127.0.0.1:5000/customers/'

payload = {
    'FName': 'Jason',
    'LName': 'Cereal',
    'PhoneNumber': 1111111114
}

response = requests.get(BASE, params=payload)

print(response.json())
