import requests
from datetime import datetime
from decouple import config, Csv
from .access_token import generate_access_token
from .utils import generate_timestamp
from .password import generate_password

# Execute all functions
formatted_time = generate_timestamp()
password = generate_password(formatted_time)
my_access_token = generate_access_token()


def lipa_na_mpesa(phonenumber, amount, shortcode, callback_url):
    print('Start excecuting the Simulate LNMOnline function:::')
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phonenumber,
        "PartyB": shortcode,
        "PhoneNumber":phonenumber,
        "CallBackURL": callback_url,
        "AccountReference": "vicks_test",
        "TransactionDesc": "Pay for internet"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    return response.text
    
