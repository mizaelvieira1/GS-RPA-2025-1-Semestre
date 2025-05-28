from fpdf import FPDF
from datetime import datetime
import pandas as pd
import os

# Gera o nome do arquivo com a data no formato DDMMYY
data_nome = datetime.now().strftime('%d%m%y')
nome_arquivo = f'Relatorio_Monitoramento_Queimadas_{data_nome}.pdf'

# Base do projeto (onde o script está rodando)
BASE_DIR = os.getcwd()

# Caminhos relativos ao projeto
CAMINHO_GRAFICO = os.path.join(BASE_DIR, 'Relatorio', 'grafico_focos.png')
CAMINHO_ALERTAS = os.path.join(BASE_DIR, 'Processamento', 'alertas.csv')
CAMINHO_RELATORIO = os.path.join(BASE_DIR, 'Relatorio', nome_arquivo)


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Relatório de Monitoramento de Queimadas", ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

def gerar_relatorio():
    pdf = PDF()
    pdf.add_page()

    # Data da análise
    data_hoje = datetime.now().strftime('%d/%m/%Y %H:%M')
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Data da análise: {data_hoje}", ln=True)

    # Nomes e RMs
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 10, "Cristiano Washington Dias | RM555992@fiap.com.br", ln=True)
    pdf.cell(0, 10, "Mizael Vieira Bezerra | RM555796@fiap.com.br", ln=True)
    pdf.cell(0, 10, "Santiago Nascimento Bernardes | RM557447@fiap.com.br", ln=True)

    # Texto explicativo
    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8,
        "Abaixo, você pode visualizar o relatório gerado automaticamente com base nos dados mais recentes de focos de queimadas obtidos do INPE. "
        "O gráfico apresenta a distribuição por estado, enquanto a tabela final resume os alertas emitidos conforme os critérios definidos pelo grupo."
    )
    pdf.ln(3)

    # Gráfico com borda e espaçamento
    if os.path.exists(CAMINHO_GRAFICO):
        y_atual = pdf.get_y()
        altura = 60  # altura visual estimada do gráfico
        pdf.image(CAMINHO_GRAFICO, x=30, y=y_atual + 3, w=150)
        pdf.set_y(y_atual + 100)  # empurra a tabela para baixo
    else:
        pdf.ln(10)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, "Gráfico não encontrado.", ln=True)
        pdf.set_text_color(0, 0, 0)

    # Tabela de alertas
    pdf.ln(15)
    pdf.set_font("Arial", "B", 12)
    pdf.set_x(30)
    pdf.cell(0, 10, "Alertas por Estado", ln=True)

    pdf.set_font("Arial", "", 11)

    if os.path.exists(CAMINHO_ALERTAS):
        df = pd.read_csv(CAMINHO_ALERTAS)

        colunas = ["estado", "total_focos", "status"]
        larguras = [60, 40, 40]

        # Cabeçalho da tabela
        pdf.set_x(30)
        for col, w in zip(colunas, larguras):
            pdf.cell(w, 8, col.upper(), border=1)
        pdf.ln()

        # Linhas da tabela
        for _, row in df.iterrows():
            pdf.set_x(30)
            for col, w in zip(colunas, larguras):
                pdf.cell(w, 8, str(row[col]), border=1)
            pdf.ln()
    else:
        pdf.set_text_color(255, 0, 0)
        pdf.cell(0, 10, "Arquivo de alertas não encontrado.", ln=True)

    # Salvar PDF com nome personalizado
    pdf.output(CAMINHO_RELATORIO)
    print(f"📄 Relatório gerado em: {CAMINHO_RELATORIO}")

if __name__ == "__main__":
    gerar_relatorio()
