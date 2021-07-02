import requests

# create response variable and send get request to rick and morty api using requests library
response = requests.get("https://rickandmortyapi.com/api/character?name=Rick")
#verify response status code is 200 (successful)
assert response.status_code == 200

#create data variable and use json() method on your response to get a data out of it
data = response.json()
# print(data)
# print(data['info']['count'])
# assert data['info']['count'] == 671

print(data['results'][0]['name'])
print(data['results'][1]['gender'])



