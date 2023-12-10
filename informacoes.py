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

    # Localizando as tabelas
    tabelas = soup.find_all('table')
    todas_tabelas = []
    
    for tabela in tabelas:
        headers = tabela.find_all('th')
        header_names = [header.get_text().strip().lower()
                        for header in headers]
        # Verifica se a tabela possui colunas com 'previsto'
        if 'previsto' in header_names:
            todas_tabelas.append(tabela)

    # Listas para armazenar os dados das colunas desejadas
    coluna9 = []
    coluna12 = []
    coluna17 = []

    # Iterando pelas tabelas encontradas
    for tabela in todas_tabelas:
        # Iterando pelas linhas da tabela
        for linha in tabela.find_all('tr'):
            # Obtendo todas as células da linha
            cells = linha.find_all('td')

            # Verificado se a linha tem pelo menos 18 células/colunas.
            if len(cells) >= 18:
                # Adicionando os dados das colunas específicas às listas
                coluna9.append(cells[9].get_text().strip())
                coluna12.append(cells[12].get_text().strip())
                coluna17.append(cells[17].get_text().strip())

    # Criando um dicionário com as colunas desejadas
    dados_desejados = {'sentido': coluna9, 'mercadoria': coluna12, 'previsto': coluna17}
    # Convertendo o dicionário em um DataFrame do Pandas
    tabela_final = pd.DataFrame(dados_desejados)
    tabela_final['Local'] = 'paranagua'
    return tabela_final


# Função para extrair dados de Santos
def extrair_dados_santos():
    url_santos = "https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/"
    # Realiza a requisição
    response = requests.get(url_santos)
    # Faz o parsing do HTML
    soup = BeautifulSoup(response.content, "html.parser")
    # Inspecionar a página
    dados_santos = []
    dados_santos_post = soup.find_all()
    print(dados_santos_post)

    return dados_santos

# Função para combinar e organizar os dados
def organizar_dados(dados_paranagua, dados_santos):
    return 0


# Chama as funções para extrair e organizar os dados
dados_paranagua = extrair_dados_paranagua()
nome_arquivo = 'tabela_paranagua.xlsx'
dados_paranagua.to_excel(nome_arquivo, index=False)

