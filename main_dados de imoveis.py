import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import sys
contador = 1
url = f'https://www.vivareal.com.br/venda/sp/araras/apartamento_residencial/?pagina={contador}'
retorno = requests.get(url)
soup = bs(retorno.text)
#Colentando a quantidade de casas na região, é utilizado para saber até quantas páginas o programa deve avançar.
qtd_houses = soup.find('strong', {'class': 'js-total-records'}).text.strip()
qtd_houses = float(qtd_houses.replace('.',''))
print(qtd_houses)
#Criação de dataframe
df = pd.DataFrame(columns=['decricao', 'endereco', 'area',
                  'quarto', 'banheiro', 'vagas', 'valor', 'wlink'])
#Em quanto a quantidade de casas(card's no site) for maior que a quantidade de linhas do DataFrame  faça:
all_houses_extract = False
while all_houses_extract == False:
    print(f'Pagina {contador} - Tamanho df {df.shape[0]} - Total de cards {qtd_houses}')
    url = f'https://www.vivareal.com.br/venda/sp/araras/apartamento_residencial/?pagina={contador}'
    retorno = requests.get(url)
    if str(retorno).strip() != '<Response [200]>':
        print(f'Request negado: {retorno}')  
        sys.exit()
    soup = bs(retorno.text)
    #Lista de cards na página.
    houses = soup.find_all('a', {'class':'property-card__content-link js-card-title'})
    contador += 1

    for house in houses:
        try:
            decricao = house.find('span',{'class':'property-card__title js-cardLink js-card-title'}).text.strip()
        except:
            decricao = None
        try:
            endereco = house.find('span',{'class':'property-card__address'}).text.strip()
        except:
            endereco = None
        try:
            area = house.find('span', {'class': 'js-property-card-detail-area'}).text.strip()
        except:
            area = None
        try:
            quarto = house.find('li', {'class': 'js-property-detail-rooms'}).find('span', {'class': 'js-property-card-value'}).text.strip() 
        except:
            quarto = None
        try:
            banheiro = house.find('li', {'class': 'js-property-detail-bathroom'}).find('span').text.strip() 
        except:
            banheiro = None
        try:
            vagas = house.find('li', {'class': 'js-property-detail-garages'}).span.text.strip()
        except:
            vagas = None
        try:
            valor = house.find('div', {'class': 'js-property-card__price-small'}).find('p').text.strip().replace('R$', '')
            #Tratamento, caso valor estiver com o campo de'Preço abaixo do mercado'
            if valor.isnumeric() == False:
                valor = valor.split(' ')[1]
        except:
            valor = None
        try:
            wlink = 'https://www.vivareal.com.br' + house['href']
        except:
            wlink = None
        #Insere registro na ultima linha do DataFrame
        df.loc[df.shape[0]] = [
            decricao,
            endereco,
            area,
            quarto,
            banheiro,
            vagas,
            valor,
            wlink
        ]
        if df.shape[0] >= qtd_houses:
            all_houses_extract = True
            break
            
            

#Remover duplicatas do df
#df = df.drop_duplicates()    
absFilePath = os.path.dirname(os.path.realpath(__file__))
arq = f'{absFilePath}\imoveis.csv'
df.to_csv(arq, encoding='utf-8', index=False, sep=';')
print(f'Arquivo imoveis.csv Exportado!')

