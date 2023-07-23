import requests

# авторизация
response=requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": "d7c56b2c30ac31ebc1c7313685c2e8de",
    "email": "dianadeyanova97609@gmail.com",
    "password": "Iloveqa1"
})
print(response.status_code)
token="d7c56b2c30ac31ebc1c7313685c2e8de"

# активация тренера
response_activated=requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email', json={
    "trainer_token": token
})
num=f'мой токен это {token}'
print(num)

# создание покемона
base_url='https://api.pokemonbattle.me:9104/'
response_add_pokemon=requests.post(f'{base_url}pokemons', headers={'trainer_token': token},
json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_add_pokemon.text)

# айди покемона
id_response = input("Введи id покемона: ")
pokemon_id = int(id_response)
print(f"Значение id: {pokemon_id}")

# изменение покемона
response_add_pokemon2=requests.put(f'{base_url}pokemons', headers={'trainer_token': token},
json={
    "pokemon_id": pokemon_id, 
    "name": "Новое имя",
    "photo": "https://dolnikov.ru/pokemons/albums/817.png"
})
print(response_add_pokemon2.text)

# поймать покемона в покебол
response_catch_a_pokemon_in_pokeball=requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token': token},
json={
    "pokemon_id": pokemon_id
})
print(response_catch_a_pokemon_in_pokeball.text)




# информация о покемонах
# response_info_pokemons=requests.get(f'{base_url}pokemons', params={'trainer_id': 1422})
# print(response_info_pokemons.text)
