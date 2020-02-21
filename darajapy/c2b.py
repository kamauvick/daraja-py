import requests
from keys import *
from access_token import generate_access_token
from decouple import config

my_access_token = generate_access_token()

def register_url(confirmation_url, validation_url):
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {"ShortCode": c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": confirmation_url,
               "ValidationURL": validation_url
               }

    response = requests.post(api_url, json=request, headers=headers)

    return response.text


def simulate_c2b_transaction(phone_number, amount):
    print('Start excecuting the Simulate C2B function:::')
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {"ShortCode": c2b_shortcode,
               "CommandID": "CustomerPayBillOnline",
               "Amount": amount,
               "Msisdn": phone_number,
               "BillRefNumber": "12345"}

    response = requests.post(api_url, json=request, headers=headers)

    return response.text
