import requests
from requests.auth import HTTPBasicAuth


def APIRequest(CompanyNumber):
    BaseURL = "https://api.company-information.service.gov.uk"

    response = requests.get(
        BaseURL + f'/company/{CompanyNumber}/persons-with-significant-control/',
        auth=HTTPBasicAuth('db9f7d86-ef5f-4157-b79a-25104fa9c4fe', '')
    )

    if 'errors' in response.json():
        return "00000000"

    for item in response.json()["items"]:
        return item["identification"]["registration_number"]
