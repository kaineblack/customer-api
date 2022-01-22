import pandas as pd
from flask import Flask
from flask_restful import Resource, Api, reqparse


# instantiate the flask app and wrap in REST API format
app = Flask(__name__)
api = Api(app)

# instantiate a request parser and define the parameters
parser = reqparse.RequestParser()
parser.add_argument('FName', type=str, required=True, help="You must enter a first name for the customer")
parser.add_argument('LName', type=str, required=True, help="You must enter a last name for the customer")
parser.add_argument('PhoneNumber', type=int, required=True, help="You must enter a phone number for the customer")


# create a customer class that takes care of the get requests as they come in
class Customer(Resource):
    """
    API resource that responds to a GET request which includes a customers first name, 
    last name, and phone number this class will respond to GET requests and return the 
    corresponding "CustomerID" for that customer profile. If the customer profile does 
    not exist in the CSV file, it will be created and the new "CustomerID" will be returned.

    Attributes
    ----------
    FName: str
        first name of the customer
    LName: str
        last name of the customer
    PhoneNumber: int
        phone number of the customer (10 digits)
    Customers: pd.DataFrame
        all current customers 

    Methods
    -------
    get:
        returns the CustomerID
    """
    def __init__(self):
        """
        Parse all of the provided information from the GET request.
        Also loads in the current state of the customers CSV file to be evaluated.
        """
        self.__FName = parser.parse_args().get('FName', None)   # first name
        self.__LName = parser.parse_args().get('LName', None)   # last name
        self.__PhoneNumber = parser.parse_args().get('PhoneNumber', None)   # phone number
        assert len(str(self.__PhoneNumber)) == 10, 'PhoneNumber must be 10 digits long' # check phone number length
        self.__Customers = pd.read_csv('customers.csv') # load in current state of CSV file

    def get(self):
        """
        Responds to GET request with CustomerID. If the customer does not exist already, adds them to the CSV file 
        and creates CustomerID for them and returns that. Also returns a bool value to indicate if the customer
        was a new customer or an existing customer.

        Returns
        -------
        dict:
            A JSON serializable dict containing the CustomerID and NewCustomer indicator.
        """

        # check to see if the phone number already exists in the CSV file 
        if self.__PhoneNumber in self.__Customers['PhoneNumber'].values.tolist():
            customer_id = int(self.__Customers['CustomerID'][self.__Customers['PhoneNumber'] == self.__PhoneNumber].values[0])
            return {'CustomerID': customer_id, 'NewCustomer': False}

        # if the customer doesn't already exist, create them and append them to the existing CSV file
        else:
            customer_id = len(self.__Customers)+1
            df_a = pd.DataFrame({
                'CustomerID': [customer_id],
                'FName': [self.__FName],
                'LName': [self.__LName],
                'PhoneNumber': [self.__PhoneNumber]
            })
            df_a.to_csv('customers.csv', mode='a', index=False, header=False)
            return {'CustomerID': customer_id, 'NewCustomer': True}


# add the Customer class as an API resource on the root URL
api.add_resource(Customer, '/')

# run the application if it is being executed directly
if __name__ == "__main__":
  app.run(debug=True)