# 🌿 Relatório Automatizado de Monitoramento de Queimadas – Global Solution RPA

Este projeto tem como objetivo utilizar tecnologias de automação e análise de dados para **monitorar focos de queimadas em tempo real**, com base nos dados abertos do INPE. O resultado é a geração de **relatórios automáticos em PDF**, contendo gráficos e alertas por estado, atualizados de forma dinâmica.

---

## 🚀 Tecnologias utilizadas

- **Python 3.10+**
- `pandas`
- `matplotlib`
- `geopandas`
- `shapely`
- `requests`
- `fpdf`

---

## 📁 Estrutura do Projeto

```
GS RPA/
├── Coleta/
│   └── baixar_dados.py
├── Dados/
│   └── (CSV baixado do INPE)
├── Processamento/
│   ├── tratar_dados.py
│   ├── geolocalizar_estados.py
│   ├── gerar_metricas.py
│   ├── alertas.csv
│   └── dados_tratados/
│       └── (CSVs tratados e com estado)
├── Geodados/
│   └── BR_UF_2024/
│       └── (arquivos .shp do shapefile IBGE)
├── Relatorio/
│   ├── gerar_relatorio.py
│   ├── grafico_focos.png
│   └── Relatorio_Monitoramento_Queimadas_DDMMYY.pdf
```

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório e instale as dependências:

```bash
pip install pandas matplotlib geopandas shapely requests fpdf
```

> Se estiver usando `geopandas`, recomenda-se instalar via `conda`, ou baixar o `.whl` compatível com seu sistema.

---

### 2. Execute os scripts na seguinte ordem:

```bash
# 1. Baixar o CSV dos últimos 10 minutos
python Coleta/baixar_dados.py

# 2. Tratar o CSV bruto
python Processamento/tratar_dados.py

# 3. Adicionar coluna 'estado' aos dados tratados
python Processamento/geolocalizar_estados.py

# 4. Gerar gráfico e alertas automáticos
python Processamento/gerar_metricas.py

# 5. Gerar o relatório final em PDF
python Relatorio/gerar_relatorio.py
```

O PDF será salvo na pasta `Relatorio/` com o nome:

```
Relatorio_Monitoramento_Queimadas_DDMMYY.pdf
```

---

## 👥 Integrantes do Grupo

- **Cristiano Washington Dias**  
  RM555992@fiap.com.br

- **Mizael Vieira Bezerra**  
  RM555796@fiap.com.br

- **Santiago Nascimento Bernardes**  
  RM557447@fiap.com.br

---

## 🧠 Proposta

A solução visa reduzir o tempo de resposta a focos de calor por meio da automação da coleta, análise e visualização de dados ambientais em tempo real — utilizando fontes oficiais e ferramentas inteligentes para apoiar a prevenção de desastres naturais no Brasil.

---
