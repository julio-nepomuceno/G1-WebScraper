import requests
from termcolor import colored
from bs4 import BeautifulSoup

link = 'https://g1.globo.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
requisicao = requests.get(link, headers=headers)
if requisicao.status_code == 200:
    site = BeautifulSoup(requisicao.text, 'html.parser')

    principais_noticias = site.find_all('a', class_="feed-post-link gui-color-primary gui-color-hover")
    total_noticias = len(principais_noticias)
    max_noticias = min(10, total_noticias)
    if total_noticias == 0:
        print(colored(f'Nenhuma notícia encontrada!', 'red'))
    else:
        for i, noticia in enumerate(principais_noticias[:max_noticias], 1):
            titulo = noticia.text.strip().upper()
            link = noticia.get("href", "Link não disponível")
            print(colored(f'{i}° {titulo}', 'light_yellow'))
            print('Link:', end=' ')
            print(colored(f'{link}', 'light_cyan'))
else:
    print(colored(f'Erro ao acessar o site! (código: {requisicao.status_code})', 'red'))