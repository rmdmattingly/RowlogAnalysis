import requests

def getData(url):
    response = requests.get(url)
    return response.json()
