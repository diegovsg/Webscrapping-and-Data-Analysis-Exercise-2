# Webscrapping-and-Data-Analysis-Exercise 2
 Objetivo é gerar um procedimento para gerar uma tabela com o volume diário previsto por produto, sentido (exportação e importação) e porto (Paranaguá, Santos). Limitamos o escopo aos portos de Paranaguá e Santos e listamos duas potenciais fontes dos dados (administrações de cada porto):1) https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroat ivo  2) https://www.portodesantos.com.br/informacoes-operacionais/operacoes- portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/


 Primeiramente me descupe pelo envio tarde do desafio, não que seja uma desculpa, mas estava na última semana de prova e não foi possivel dedicar 100% ao desafio.

 Inicialmente eu consegui desenvolver foi analisar e pegar os dados do porto de santos, entretanto, tive que interpretar um pouco. Pensei que Sentido fosse o emb e desenbarque  e troquei por exportar e importar, para ficar semelhante ao que foi pedido, o previsto peguei o peso que tinha disponivel no site e por fim a mercadoria tinha seu nome na tabela. O nome do porto coloquei adicional depois. 
 
 Após tentei fazer o mesmo com o porto de paranagua, mas obtive uns problemas principalmente por ter colunas diferentes entre todas as tabelas, não consegui pegar certinho as tabelas, consegui da primeira tabela, pegando as tabelas por indice, como fiz em santos, ou seja, verifiquei pelo numero de colunas se fosse o mesmo numero pegaria informações dessa coluna, mas não vai funcionar pelo motivo já citado. Porém deixo minha ideia de como procederia no código: A ideia era verificar pelo nome da coluna e só conseguir pegar as informações das linhas, analisadas, pertencente a coluna desejada, mas não conseegui implementar essa ideia. O nome do porto adicionei por codigo também, no caso de paranagua.

Separei em 3 funções para pegar a tabela de cada porto em duas funcoes separadas e uma ultima para unir as
duas tabelas.

Acredito que para continuar a desenvolver precisaria validar se as informações tiradas estão corretas, ou seja, os termos, depois tentar conseguir as ideias funcionarem como a de pegar as informações de parangua verificando a coluna e ai pegando as informações da linha somente das colunas desejadas. Depois unir corretamente as tabelas e por fim retirar análises dessa tabela. Como as toneladas previsas para cada porto, 
se o porto exporta ou importa mais e o produto que tem o maior volume previsto.

Por fim grato pela oportunidade, 
vou tentar ainda o desafio como aprendizagem, então grato pela oportunidade.

Diego