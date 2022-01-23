# Simple Customer API
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
