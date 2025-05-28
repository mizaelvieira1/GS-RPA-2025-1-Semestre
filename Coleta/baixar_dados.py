import os
import requests
import urllib3
from datetime import datetime

# Desativa alertas de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_nome_arquivo():
    agora = datetime.now()

    # Arredonda os minutos para o múltiplo de 10 anterior
    minutos_10 = (agora.minute // 10) * 10
    horario_formatado = agora.replace(minute=minutos_10, second=0, microsecond=0)

    nome = f'focos_10min_{horario_formatado.strftime("%Y%m%d_%H%M")}.csv'
    return nome

def baixar_dados():
    base_url = 'https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/10min/'
    nome_arquivo = get_nome_arquivo()
    url = base_url + nome_arquivo

    # Caminho absoluto da pasta 'dados' relativa à raiz do projeto
    base_dir = os.getcwd()
    pasta_dados = os.path.join(base_dir, 'dados')
    destino = os.path.join(pasta_dados, nome_arquivo)

    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        os.makedirs(pasta_dados, exist_ok=True)

        with open(destino, 'wb') as f:
            f.write(response.content)

        print(f'Download realizado com sucesso: {nome_arquivo}')
        return destino

    except Exception as e:
        print(f'Erro ao baixar o arquivo: {e}')
        return None

if __name__ == "__main__":
    baixar_dados()
