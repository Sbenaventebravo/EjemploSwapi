import requests

def obtener_personajes():
    url = "https://swapi.dev/api/people"
    request = requests.get(url)
    return request.json()

def obtener_naves():
    url = "https://swapi.dev/api/starships"
    request = requests.get(url)
    return request.json()