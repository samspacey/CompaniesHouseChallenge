def APIRequest(CompanyNumber):

    response = requests.get(
    BaseURL + f'/company/{CompanyNumber}/persons-with-significant-control/',
    auth=HTTPBasicAuth('db9f7d86-ef5f-4157-b79a-25104fa9c4fe', '')
    )
    return response
