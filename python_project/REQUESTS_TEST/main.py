import requests
import json
token = 'f68152a85ba4e5c8e7bc24cb9b9aa3c9'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers ={'Content-Type': 'application/json', 'trainer_token': token}, json = {
    "name": "ИВИ",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response.json)
pokemon_id = response.json()['id']
response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers ={'Content-Type': 'application/json', 'trainer_token': token}, json ={
    "pokemon_id": pokemon_id,
    "name": "Addd",
    "photo": ""
})
print(response_change.json)

response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers ={'Content-Type': 'application/json', 'trainer_token': token}, json ={
    "pokemon_id": pokemon_id
})
print(response_change.json)