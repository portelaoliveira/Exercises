"""
# Necessário instalar a biblioteca "requests" para importação

import requests

try:
    # A variável "response" recebe o objeto Response gerado pela requisição de metodo GET
    url = 'http://www.pudim.com.br/'
    response = requests.get(url)

    print(f'\n\33[32m{" CONEXÃO REALIZADA ":-^43}')
    print('Parece que você CONSEGUIU entrar no site...')
    print(f'URL: {url}'.center(43))
