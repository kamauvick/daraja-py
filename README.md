# daraja-py
Implementing Daraja API services 

  

## Implemented Features
 - [x] Lipa na mpesa online
 - [x] C2B
 - [ ]  B2C

## Installation
> To install the library using pip, run;

`pip install daraja-py`

## Required parameters
> #### Lipa na Mpesa
* phone_number
* amount
* BusinessShortCode
* CallBackURL

> #### C2B
##### register url
* ConfirmationUrl
* ValidationUrl

##### simulate transaction
* phone_number
* amount

## Usage

```python
from darajapy import lipanampesa, c2b

lmn = lipanampesa.lipa_na_mpesa(
				'07XXXXXXXX',
				'500',
				'324XXXX',
				'https://www.somecallbackurl.com'
				)

# The register transaction is only run once
c2b_register = c2b.register_url(
	'https://www.someconfirmationurl.com',
	'https://www.somevalidationurl.com'
	)

c2b_simulate_transaction = c2b.simulate_c2b_transaction(
			   '07XXXXXXXX',
			   '500'
			   )
```

##