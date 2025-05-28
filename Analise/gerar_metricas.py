import os
import pandas as pd
import matplotlib.pyplot as plt

# Base do projeto (raiz onde o script está sendo rodado)
BASE_DIR = os.getcwd()

# Caminhos relativos
PASTA_TRATADOS = os.path.join(BASE_DIR, 'Processamento', 'dados_tratados')
CAMINHO_ALERTAS = os.path.join(BASE_DIR, 'Processamento', 'alertas.csv')
CAMINHO_GRAFICO = os.path.join(BASE_DIR, 'Relatorio', 'grafico_focos.png')

def encontrar_csv_com_estado():
    arquivos = [f for f in os.listdir(PASTA_TRATADOS) if f.endswith('_com_estado.csv')]
    if not arquivos:
        raise FileNotFoundError("❌ Nenhum arquivo com coluna 'estado' encontrado.")
    caminhos = [os.path.join(PASTA_TRATADOS, f) for f in arquivos]
    return max(caminhos, key=os.path.getmtime)

def gerar_metricas(caminho_csv):
    df = pd.read_csv(caminho_csv)
    print(f'\n✔️ Arquivo carregado: {os.path.basename(caminho_csv)}')
    print(f'🔍 Colunas disponíveis: {df.columns.tolist()}')

    if 'estado' in df.columns:
        total_estado = df['estado'].value_counts()
        print("\n📊 Total de focos por estado:")
        print(total_estado)

        # Gera e salva gráfico
        total_estado.plot(kind='bar', title='Focos por Estado')
        plt.xlabel('Estado')
        plt.ylabel('Número de Focos')
        plt.tight_layout()
        plt.savefig(CAMINHO_GRAFICO)
        plt.close()

        # Gerar alertas automáticos
        alertas = []
        for estado, total in total_estado.items():
            status = 'CRÍTICO' if total >= 5 else 'OK'
            alertas.append({'estado': estado, 'total_focos': total, 'status': status})

        # Salvar em CSV
        df_alertas = pd.DataFrame(alertas)
        df_alertas.to_csv(CAMINHO_ALERTAS, index=False)
        print(f'\n🚨 Alertas salvos em: {CAMINHO_ALERTAS}')
        print(df_alertas)

    else:
        print("⚠️ Coluna 'estado' não encontrada.")

if __name__ == "__main__":
    caminho = encontrar_csv_com_estado()
    gerar_metricas(caminho)
