import requests
from bs4 import BeautifulSoup
import pandas as pd

def extrair_dados_paranagua():
    url_paranagua = "https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo"
    # Realiza a requisição
    response = requests.get(url_paranagua)
    if response.status_code == 200:
        # Faz o parsing do HTML
        soup = BeautifulSoup(response.content, "html.parser")
        # Encontra todas as tabelas
        tabelas_previstas = []

        tabelas = soup.find_all('table')
        for table in tabelas:
            headers = table.find_all('th')
            header_names = [header.get_text().strip().lower() for header in headers]

            # Verifica se a tabela possui colunas com 'previsto'
            if 'previsto' in header_names:
                tabelas_previstas.append(table)

        # Criar um DataFrame vazio para consolidar os dados
        df_consolidado = pd.DataFrame(columns=['Produto', 'Previsto', 'Sentido', 'Porto'])

        # Para cada tabela com 'previsto', extrair dados e adicionar ao DataFrame consolidado
        for table in tabelas_previstas:
            linhas = table.find_all('tr')
            for linha in linhas[1:]:  # Começa a partir da segunda linha para evitar o cabeçalho
                colunas = linha.find_all(['td', 'th'])
                dados_linha = [coluna.get_text().strip() for coluna in colunas]

                # Se houver 4 colunas (produto, previsto, sentido e outra), adicione ao DataFrame consolidado
                if len(dados_linha) == 4:
                    df_consolidado = df_consolidado.append({
                        'Produto': dados_linha[0],
                        'Previsto': dados_linha[1],
                        'Sentido': dados_linha[2],
                        'Porto': 'Paranaguá'
                    }, ignore_index=True)

        return df_consolidado

    else:
        print('A requisição falhou')

# Chamada da função para extrair os dados
df_final = extrair_dados_paranagua()

# Mostra o DataFrame consolidado
print(df_final)


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
# dados_santos = extrair_dados_santos()
# dados_combinados = organizar_dados(dados_paranagua, dados_santos)

# Salva os dados em um arquivo CSV
# dados_combinados.to_csv('dados_volume_diario_previsto.csv', index=False)
