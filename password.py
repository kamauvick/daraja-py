import base64
from keys import *

# Generate password
def generate_password(formatted_time):
    data_to_encode = (
        business_shortCode + lipa_na_mpesa_passkey + formatted_time
    )
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode("utf-8")
    return decoded_password
