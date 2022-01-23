# Simple Customer API
### API Diagram:
<img src="https://user-images.githubusercontent.com/72955075/150661469-3635394b-d37b-490b-a67c-ee103092b63b.png" alt="drawing" width="800"/>



#### Receives a `GET` request from a client which contains customer information:
```python
# sample format of get request
{
  'FName': 'Kaine', 
  'LName': 'Black',
  'PhoneNumber': 9021112222
}
```

#### Returns the "CustomerID" if the customer exists in the CSV file, or creates a new customer in the CSV file if they don't exist and then returns the new CustomerID:
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
