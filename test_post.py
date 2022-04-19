import requests
import json

def test_insert_user():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    url = 'http://127.0.0.1:8000/create-usuario/'

    new_user = '{"user_id": 3, "dt_nascimento": "20-08-1995", "nome": "Thais de Maria", "user_cpf": "12312312312"}'
    new_user = json.loads(new_user)

    resposta = requests.post(url, headers=headers, data=new_user)
    resposta_dict = resposta.json()

    if resposta.status_code == 200:
        status = resposta_dict['status']
        assert status == 'success'
    else:
        assert False

