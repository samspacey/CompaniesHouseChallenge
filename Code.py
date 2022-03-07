import requests
import json

from requests.auth import HTTPBasicAuth


BaseURL = "https://api.company-information.service.gov.uk"

response = requests.get(
    BaseURL + '/company/02373469/persons-with-significant-control/',
    auth=HTTPBasicAuth('db9f7d86-ef5f-4157-b79a-25104fa9c4fe', '')
)

jsonstring = json.dumps(response.json())
parsed = json.loads(jsonstring)
print(json.dumps(parsed, indent=2, sort_keys=True))

for item in response.json()["items"]:

    print(item["name"])

while companyname != "empty"

