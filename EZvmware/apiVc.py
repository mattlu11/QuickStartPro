import requests

def getSession(vc: str, user: str, password: str):
    vcUrl = 'https://' + vc + '/rest/com/vmware/cis/session'
    userName = user
    userPassword = password
    auth = (userName, userPassword)
    response = requests.post(vcUrl, headers={'Accept': 'application/json'}, auth=auth, verify=False)
    sessionId = response.json()['value']
    return sessionId


def getVcService(vc: str, token: str):
    serviceUrl = 'https://' + vc + '/api/vcenter/services'
    serviceResponse = requests.get(serviceUrl, headers={'vmware-api-session-id': token}, verify=False)
    serviceResponseCode = serviceResponse.status_code
    if serviceResponseCode == 200:
        responseData = serviceResponse.json()
        return responseData
    else:
        print("Error")

def handleServiceData(vc: str, data: dict):
    healthCount = 0
    unhealthNames = []
    for serviceName, serviceInfo in data.items()
    if "health" in serviceInfo:
        healthCount += 1
        if serviceInfo["health"] != "HEALTHY":
            unhealthNames.append(serviceName)

    print(f"Number of detected services: {healthCount}")
    if unhealthNames:
        print(f"Unhealth Name: {unhealthNames}")
    else:
        print("All services are HEALTHY")