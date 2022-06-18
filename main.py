import json

import requests
name = "+998910080886"
url = f'http://127.0.0.1:8000/api/v1/getcourse/123456789/'
response = requests.get(url)
print(response.text)