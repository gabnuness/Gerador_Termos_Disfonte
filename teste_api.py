
# arquivo para testes de API

from dotenv import load_dotenv
import os
import requests
from functions import campo_formatado
load_dotenv()
api_chave = os.getenv("API_AUTENTIQUE")


#endpoint graphQL
url = "https://api.autentique.com.br/v2/graphql"

# Autenticação com API para cada requisição
headers = {
    "Authorization" : f"Bearer {api_chave}",
    "Content-Type" : "application/json"
}

# corpo da requisição
# aqui foi criado um dicionario para a query, limita 10 itens por pagina, mostra o total de itens e os dados do item (id, nome e quando foi criado)
body = {   
}


# requests Python
resposta = requests.post(url, headers=headers, json=body) # dentro da ruquest tipo POST, você passa os parâmetros url(que seria o endpoint), o cabeçalho (que foi definido, para autenticar) e o JSON

print(resposta.status_code) # código http
dados = resposta.json()

'''OBS: o json=body é convertido para JSON na requisição de IDA, pois a API espera esse formato, dentro de dados, foi convertido a respost.json() para a VOLTA da requisição, apesar da mesma funcionalidades, são para usos diferentes, são independentes'''

if "errors" in dados:
    print("Algo deu errado", dados["errors"])
else:
    print(f"Dados: {dados}")