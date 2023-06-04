import requests
import pytest

url='https://pokemonbattle.me:9104/'
token='a64b9fa06bf1159f0a649558ea12f3a3'

def test_status_code():
   
    response=requests.get(f'{url}trainers')
    assert response.status_code == 200

def test_part_of_body(): 
    response=requests.get(f'{url}trainers', params={"trainer_id":"4281"})
    assert response.json()["trainer_name"] == "Карим"
