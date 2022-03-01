import requests
import json

from requests.auth import HTTPBasicAuth


BaseURL = "https://api.company-information.service.gov.uk"

payload = {'q': 'VODAPHONE LIMITED'}

response = requests.get(
    BaseURL + '/company/02373469/persons-with-significant-control/',
    auth=HTTPBasicAuth('db9f7d86-ef5f-4157-b79a-25104fa9c4fe', '')
)

print(response.json())

#json.loads(response.json())
