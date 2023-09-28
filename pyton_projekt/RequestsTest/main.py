import requests
response=requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    "name": "generate",
    "photo": "generate"
}, headers={'Content-Type':'application/json', 'trainer_token': '5f8343da0ae32812fce0cbaff9526a3c'})

print(response.text)

requests_rename=requests.put('https://api.pokemonbattle.me:9104/pokemons', json={
    "pokemon_id": "11383",
    "name": "New Nam",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers={'Content-Type':'application/json', 'trainer_token': '5f8343da0ae32812fce0cbaff9526a3c'})

print(requests_rename.text)

requests_catch=requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball' ,json={
    "pokemon_id": "11383"
}, headers={'Content-Type':'application/json', 'trainer_token': '5f8343da0ae32812fce0cbaff9526a3c'})

print(requests_catch.text)