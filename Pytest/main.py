import requests

url='https://pokemonbattle.me:9104/'
token='a64b9fa06bf1159f0a649558ea12f3a3'
response=requests.post(f'{url}pokemons', headers={'trainer_token' : token}, json={
"name":"pickachu",
"photo":"https://dolnikov.ru/pokemons/albums/002.png"
})
print(response.json())


response_change_name=requests.put(f'{url}pokemons', headers={'trainer_token' : token}, json={
"pokemon_id":"12888",
"name":"raichu",
"photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(response_change_name.json())


response_pokeball=requests.post(f'{url}trainers/add_pokeball', headers={'trainer_token' : token}, json={
"pokemon_id":"12888",
})
print(response_pokeball.json())
