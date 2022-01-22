import requests

BASE = 'http://127.0.0.1:5000/'

payload = {
    'FName': 'Kaine', 
    'LName': 'Black',
    'PhoneNumber': 1111111111
}

response = requests.get(BASE, params=payload)

print(response.json())