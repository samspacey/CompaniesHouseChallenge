import requests
import json
from APIRequests import APIRequest


from requests.auth import HTTPBasicAuth


companynumber = "02373469"

while companynumber != "00000000":
    #APIRequest(companynumber.rjust(8, "0"))
    companynumber = APIRequest(companynumber.rjust(8, "0"))
    print(companynumber)