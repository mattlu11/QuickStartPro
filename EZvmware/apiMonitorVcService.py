import requests
from apiVc import getSession, getVcService, handleServiceData



if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()

    vc1 = "host1"
    vc2 = "host2"

    hosts = [vc1, vc2]
    user = "user"
    password = "password"

    for host in hosts:
        sessionStr = getSession(host, user, password)
        data = getVcService(host, sessionStr)
        handleServiceData(host, data)