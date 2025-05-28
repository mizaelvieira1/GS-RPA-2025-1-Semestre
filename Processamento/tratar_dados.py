import os
import pandas as pd

# Base do projeto
BASE_DIR = os.getcwd()

# Caminhos relativos
PASTA_DADOS = os.path.join(BASE_DIR, 'Dados')
PASTA_SAIDA = os.path.join(BASE_DIR, 'Processamento', 'dados_tratados')

def encontrar_csv_mais_recente():
    arquivos = [f for f in os.listdir(PASTA_DADOS) if f.endswith('.csv')]
    if not arquivos:
        raise FileNotFoundError("❌ Nenhum arquivo CSV encontrado na pasta Dados.")
    
    caminhos = [os.path.join(PASTA_DADOS, f) for f in arquivos]
    mais_recente = max(caminhos, key=os.path.getmtime)
    return mais_recente

def tratar_csv(caminho_csv):
    try:
        # Tenta abrir com UTF-8, senão tenta ISO-8859-1
        try:
            df = pd.read_csv(caminho_csv, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(caminho_csv, encoding='ISO-8859-1')

        print(f'\n✔️ Arquivo lido: {os.path.basename(caminho_csv)}')

        # Padroniza nomes de colunas
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

        # Remove colunas completamente vazias
        df.dropna(axis=1, how='all', inplace=True)

        # Preenche valores ausentes com "N/D"
        df.fillna('N/D', inplace=True)

        # Garante que a pasta de saída existe
        os.makedirs(PASTA_SAIDA, exist_ok=True)

        # Monta nome e caminho do novo arquivo
        nome_base = os.path.basename(caminho_csv).replace('.csv', '_tratado.csv')
        caminho_saida = os.path.join(PASTA_SAIDA, nome_base)

        # Salva arquivo tratado
        df.to_csv(caminho_saida, index=False)
        print(f'✅ Arquivo tratado salvo em: {caminho_saida}\n')
        return caminho_saida

    except Exception as e:
        print(f'❌ Erro ao tratar CSV: {e}')
        return None

if __name__ == "__main__":
    caminho_csv = encontrar_csv_mais_recente()
    tratar_csv(caminho_csv)
