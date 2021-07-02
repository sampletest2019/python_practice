import requests

# create response variable and send get request to rick and morty api using requests library
response = requests.get("https://rickandmortyapi.com/api/character")
#verify response status code is 200 (successful)
assert response.status_code == 200
