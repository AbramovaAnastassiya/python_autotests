import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code ==200

def test_of_body_response():
    response = requests.get('https://pokemonbattle.me:5000/pokemons', params= {'trainer_id': '1844' })  
    assert response.json()['name'] =='NA'