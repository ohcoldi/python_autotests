import requests
import pytest

def test_status_code():
    token='d7c56b2c30ac31ebc1c7313685c2e8de'
    response=requests.post('https://api.pokemonbattle.me:9104/pokemons', headers={'trainer_token': token}, json={ 
    "name": "Кум",
    "photo": "https://dolnikov.ru/pokemons/albums/056.png"
})
    # я утверждаю,что 
    #== сравнение
    assert response.status_code == 201
    
    
    def test_part_of_body():
        response=requests.get('https://api.pokemonbattle.me:9104/trainers', params={'trainer_id' : 1810})
        response_body=response.text
        assert response.json()['trainer_name'] == 'Диана'
    
    @pytest.mark.parametrize('key, value', [('trainer_name', 'Диана'), ('city', 'Москва')])
    def test_part_of_body(key, value):
        response=requests.get('https://api.pokemonbattle.me:9104/trainers', params={'trainer_id' : 1810})
        assert response.json()[key] == value