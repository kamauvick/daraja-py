import requests
from requests.auth import HTTPBasicAuth
from .keys import *
#Generate an access_token
def generate_access_token():
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(
            consumer_key, consumer_secret))
    except:
        r = requests.get(api_URL, auth=HTTPBasicAuth(
            consumer_key, consumer_secret), verify=False)

    json_response = r.json()

    my_access_token = json_response["access_token"]
    return my_access_token
