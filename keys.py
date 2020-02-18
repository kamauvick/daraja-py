from decouple import config, Csv

consumer_key = config("ConsumerKey")
consumer_secret = config("ConsumerSecret")

business_shortCode = config("BusinessShortCode")  # Lipa Na Mpesa Shortcode
lipa_na_mpesa_passkey = config("LipaNaMpesaPasskey")
c2b_shortcode = config('C2B_SHORTCODE')
msisnd = config('MSISDN')
