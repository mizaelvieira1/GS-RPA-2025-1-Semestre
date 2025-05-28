import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import os

# Base do projeto (raiz onde o script está sendo executado)
BASE_DIR = os.getcwd()

# Caminhos relativos
PASTA_TRATADOS = os.path.join(BASE_DIR, 'Processamento', 'dados_tratados')
PASTA_SHAPE = os.path.join(BASE_DIR, 'Geodados', 'BR_UF_2024')
SHAPEFILE_ESTADOS = os.path.join(PASTA_SHAPE, 'BR_UF_2024.shp')

def localizar_estado(caminho_csv):
    # Carrega focos tratados
    df = pd.read_csv(caminho_csv)

    # Converte lat/lon em ponto geográfico
    df['geometry'] = df.apply(lambda row: Point(row['lon'], row['lat']), axis=1)
    gdf_focos = gpd.GeoDataFrame(df, geometry='geometry', crs='EPSG:4326')

    # Carrega shapefile dos estados
    gdf_estados = gpd.read_file(SHAPEFILE_ESTADOS).to_crs('EPSG:4326')

    # Junta focos + estados com base espacial
    gdf_resultado = gpd.sjoin(gdf_focos, gdf_estados[['geometry', 'NM_UF']], how='left', predicate='within')

    # Renomeia para "estado"
    gdf_resultado.rename(columns={'NM_UF': 'estado'}, inplace=True)

    # Salva novo CSV com coluna "estado"
    novo_nome = caminho_csv.replace('_tratado.csv', '_com_estado.csv')
    gdf_resultado.drop(columns='geometry').to_csv(novo_nome, index=False)
    print(f'✅ CSV com coluna "estado" salvo em:\n{novo_nome}')

if __name__ == "__main__":
    arquivos = [f for f in os.listdir(PASTA_TRATADOS) if f.endswith('_tratado.csv')]
    caminhos = [os.path.join(PASTA_TRATADOS, f) for f in arquivos]
    mais_recente = max(caminhos, key=os.path.getmtime)

    localizar_estado(mais_recente)
