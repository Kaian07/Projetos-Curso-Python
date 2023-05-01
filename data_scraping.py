import requests
from bs4 import BeautifulSoup
import pprint

# fazendo a request do site usando scraping com BeautifulSoup.
# fazendo 2 requests porque são 2 páginas dos site para fazer o scraping.
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# Usando BeautifulSoup para analisar a pagina e obter como HTML.
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# Selecionando os links de cada tópico do site em forma de lista.
links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')
# Selecionando os subtextos da cada tópico do site em forma de lista.
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

# juntando as duas listas em uma só de links e subtextos.
mega_links = links + links2
mega_subtexts = subtext + subtext2


# Função para ordenar os tópico dos mais votados para os menos votados.
def sort_stories_list(hnew):
    return sorted(hnew, key=lambda k: k['votes'], reverse=True)


# Função que irá receber a lista de links e subtextos dos tópicos do site ira retornar um
# dicionário com nome, link e votos que recebeu.
def create_custom_hn(_links, _subtext):
    hn = []
    # Fazendo um loop para passar por cada tópico enumerando com indices.
    for idx, item in enumerate(_links):
        # Recolhendo o titúlo de cada tópico.
        title = item.getText()
        # Recolhendo o link de cada tópico.
        href = item.get('href', None)
        # Recolhendo os votos de cada tópico.
        vote = _subtext[idx].select('.score')
        # Condição para ver quais tópicos tem votos, para não dar erro de votos inexistentes.
        if len(vote):
            # Convertendo string votos em int para identificar quais tópicos tem de 100 votos ou mais.
            points = int(vote[0].getText().replace(' points', ''))
            # Condição para selecionar tópicos com 100 votos ou mais.
            # e depois adicionar a lista hn do inicio da função.
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
    return sort_stories_list(hn)


# Função pprint é para imprimir o text de forma mais organizada ja que apresenta como arquivo html.
pprint.pprint(create_custom_hn(mega_links, mega_subtexts))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
