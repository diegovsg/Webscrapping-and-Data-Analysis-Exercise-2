import requests
from bs4 import BeautifulSoup
import pandas as pd


import requests
from bs4 import BeautifulSoup
import pandas as pd

def extrair_dados_paranagua():
    # URL da página a ser acessada
    url = 'https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo'

    # Realizando a requisição para obter o conteúdo da página
    response = requests.get(url)

    # Analisando o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrando todas as tabelas na página
    tables = soup.find_all('table')

    # Inicializando um DataFrame vazio para armazenar os dados de todas as tabelas
    dados_concatenados = pd.DataFrame()

    # Iterando sobre as 7 primeiras tabelas
    for table in tables[:7]:
        # Mapeando os índices corretos das colunas de interesse
        colunas_indices = [9, 12, 17]  # Colunas desejadas na tabela (lembre-se que a contagem começa em 0)
        colunas_names = ['Sentido', 'Mercadoria', 'Previsto']  # Nomes correspondentes às colunas selecionadas

        # Criando um DataFrame temporário para armazenar os dados desta tabela
        dados_temp = pd.DataFrame(columns=colunas_names)
        dados_temp['porto'] = 'paranagua'  # Adicionando a coluna "porto" com o valor "paranagua"

        # Pegando os dados da tabela por linha
        for linha in table.findAll('tr'):
            linha = [cell.getText().strip() for i, cell in enumerate(linha.findAll('td')) if i in colunas_indices]
            if len(linha) == len(colunas_names):
                inserir_linha = pd.DataFrame([linha], columns=colunas_names)
                inserir_linha['porto'] = 'paranagua'
                dados_temp = pd.concat([dados_temp, inserir_linha], ignore_index=True)

        # Concatenando os dados desta tabela ao DataFrame principal
        dados_concatenados = pd.concat([dados_concatenados, dados_temp], ignore_index=True)

    nome_arquivo = 'tabela_paranagua_concatenada.xlsx'
    dados_concatenados.to_excel(nome_arquivo, index=False)
    return dados_concatenados

# Função para extrair dados de Santos
def extrair_dados_santos():
    url_santos = "https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/"
    # Realiza a requisição
    response = requests.get(url_santos)
    # Faz o parsing do HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrando todas as tabelas na página
    tables = soup.find_all('table', id='esperados')

    # Inicializando um DataFrame vazio para armazenar os dados de todas as tabelas
    dados_concatenados = pd.DataFrame()

    # Iterando sobre as 7 primeiras tabelas
    for table in tables:
        # Mapeando os índices corretos das colunas de interesse
        colunas_indices = [7, 8, 9]  # Colunas desejadas na tabela (lembre-se que a contagem começa em 0)
        colunas_names = ['Sentido', 'Mercadoria', 'Previsto']  # Nomes correspondentes às colunas selecionadas

        # Criando um DataFrame temporário para armazenar os dados desta tabela
        dados_temp = pd.DataFrame(columns=colunas_names)
        dados_temp['porto'] = 'Santos'  # Adicionando a coluna "porto" 

        # Pegando os dados da tabela por linha
        for linha in table.findAll('tr'):
            linha = [cell.getText().strip() for i, cell in enumerate(linha.findAll('td')) if i in colunas_indices]
            if len(linha) == len(colunas_names):
                # Substituindo os valores na coluna 'Mercadoria' conforme necessário
                if 'EMB' in linha[1].lower() and 'DESC' in linha[1].lower():
                    linha[1] = 'imp exp'
                elif 'EMB' in linha[1].lower():
                    linha[1] = 'exp'
                elif 'DESC' in linha[1].lower():
                    linha[1] = 'imp'
                inserir_linha = pd.DataFrame([linha], columns=colunas_names)
                inserir_linha['porto'] = 'santos'
                dados_temp = pd.concat([dados_temp, inserir_linha], ignore_index=True)

        # Concatenando os dados desta tabela ao DataFrame principal
        dados_concatenados = pd.concat([dados_concatenados, dados_temp], ignore_index=True)

    nome_arquivo = 'tabela_santos_concatenada.xlsx'
    dados_concatenados.to_excel(nome_arquivo, index=False)  # Salvar como arquivo Excel sem índices
    
    return dados_concatenados

# Função para combinar e organizar os dados
def organizar_dados(dados_paranagua, dados_santos):
    dados_concatenados = pd.concat([dados_santos, dados_paranagua], ignore_index=True)
    nome_arquivo = 'tabela_volume_diario.xlsx'
    dados_concatenados.to_excel(nome_arquivo, index=False)  # Salvar como arquivo Excel sem índices
    
    return dados_concatenados

santos_porto = extrair_dados_santos()
paranagua_porto = extrair_dados_paranagua()
dados_finais = organizar_dados(paranagua_porto, santos_porto)