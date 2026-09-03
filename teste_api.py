from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_chave = os.getenv("API_AUTENTIQUE")


url = "https://api.autentique.com.br/v2/graphql"

headers = {
    "Authorization" : f"Bearer {api_chave}",
    "Content Type" : "application/json"
}

corpo = {
    "query" : "{ documents(limit: 10, page: 1) {total data { id name }}}"
}

resposta = requests.post(url, headers=headers, json=corpo)
print(resposta.status_code)
dados = resposta.json()

if "errors" in dados:
    print("Algo deu errado", dados["errors"])
else:
    print(f"Dados: {dados}")