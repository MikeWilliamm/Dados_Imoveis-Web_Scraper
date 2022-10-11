## Objetivo
Extrair informações de todos os imoveis a venda no site [Vivareal](www.vivareal.com.br) em uma cidade especifica.
<p align="center">
  <img  src="prints/1site.png">
</p>

## Solução proposta
<b>Stacks:</b> Python com libs requests, bs4, pandas, os e sys.

<b>Arquitetura:</b> A arquitetura do Web Scraper obedece etapas hierárquicas, onde primeiramente teremos um raspador que vai indicar quantos imoveis/card's existem para serem acessados, com isso, o programa pode saber quantas páginas ainda pode avançar, os raspadores de dados que vão operar dentro de cada imovel/card coletara os dados de <b>[decricao]</b>, <b>[endereco]</b>, <b>[area]</b> em metros quadrados, <b>[quantidade]</b> de quartos, quantidade de <b>[banheiros]</b>, quantidade de <b>[vagas]</b>, <b>[valor]</b> e <b>[link]</b> unico do imovel. É necessário definir o estado e cidade a ser pesquisada no link de requesição.
<p align="center">
  <img  src="prints/2objetivo.png">
</p>

## Resultados
Problemas resolvidos: Durante a análise da página e de seu código HTML, foi constatado que não existe a informação do numero de páginas que determinada cidade possui, para resolver o problema, foi extraido o numero de imoveis/card's totais, com essa informação o programa avança trocando de pagina até que o tamanho do DataFrame seja igual a quantidade de imoveis/card's.

Métricas de resultado: É possivel constatar o correto funcionamento do programa atraves do numero de registros coletados, a quantidade de imoveis informada no site sempre confere com a quantidade de registros no arquivo final, atravez de validação manual feita utilizando a cidade de araras como exemplo, é possivel constatar a consistencia dos dados coletados.

Métricas de performace: Para garantir o acesso a todas as páginas necessárias, é feito uma verificação em cada requisição, caso a resposta recebida for diferente do codigo 200, o programa para instantaneamente, informa o problema e não salva o arquivo com dados incompletos.

Projetos futuros: Como projeto futuro, pode-se ser feito uma análise nos dados, onde primeiramente será extraido um média geral do valores, a partir disso identificar os bairros que possuem imoveis com o valor abaixo da média ou acima da média.