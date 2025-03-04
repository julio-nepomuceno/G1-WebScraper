import requests
from termcolor import colored
from bs4 import BeautifulSoup

link = 'https://g1.globo.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, 'html.parser')

principais_noticias = site.find_all('a', class_="feed-post-link gui-color-primary gui-color-hover")
for i, noticia in enumerate(principais_noticias[:4], 1):
    titulo = noticia.text.strip().upper()
    link = noticia["href"]
    print(colored(f'{i}° {titulo}', 'light_yellow'))
    print('Link:', end=' ')
    print(colored(f'{link}', 'light_cyan'))