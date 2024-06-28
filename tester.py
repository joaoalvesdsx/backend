import requests
import time

# URL do serviço no Render


# Função para fazer uma requisição GET ao serviço
def ping_service():
    url = "https://backend-5eid.onrender.com"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Serviço ativo: {response.status_code}")
        else:
            print(f"Falha ao acessar o serviço: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

# Loop para fazer a requisição a cada 15 minutos (900 segundos)
while True:
    ping_service()
    time.sleep(600)
