# Simple Flask API
Hi there! 👋🏼 

This repository contains a simple API built using the Flask framework. The API is used to check customer information against a customer database. A user will send a GET request which contains a payload of the users first name, last name, and phone number. The API will check the information provided against a CSV file containing all of the current customers, and if the customer exists will respond with the customer id. If the customer is not yet in the CSV file, it will add them to the file and return a newly created customer id for that individual with an indicator that they were newly created.

### API Diagram:
<img src="https://user-images.githubusercontent.com/72955075/150661534-8ab90a63-5979-4d7e-9f7b-cb17ef527183.png" alt="drawing" width="800"/>



#### Sample of GET request:
```python
# sample format of get request
{
  'FName': 'Kaine', 
  'LName': 'Black',
  'PhoneNumber': 9021112222
}
```

#### Sample API Response:
```python
# sample response if customer already exists
{
  'CustomerID': 1,
  'NewCustomer': False
}

# sample response if customer is created
{
  'CustomerID': 4,
  'NewCustomer': True
}
```
