import re
from bs4 import BeautifulSoup
import requests
import os

def clean_title(title):
    # Eliminar caracteres especiales del título
    clean_title = re.sub(r'[^\w\s]', '', title)
    # Reemplazar espacios en blanco con guiones bajos
    clean_title = clean_title.replace(' ', '_')
    return clean_title

url = 'https://www.gutenberg.org/browse/scores/top#books-last1'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')
h2_element = soup.find('h2', text='Top 100 EBooks yesterday')
book_list = h2_element.find_next('ol').find_all('a')

for book_link in book_list:
    book_url = 'https://www.gutenberg.org' + book_link['href']
    book_response = requests.get(book_url)
    book_html = book_response.text
    book_soup = BeautifulSoup(book_html,'html.parser')

    download_link = book_soup.find('a', title='Download', text='Plain Text UTF-8')
    if download_link:
        download_url = 'https://www.gutenberg.org' + download_link['href']
        book_content = requests.get(download_url).text

        book_title = book_link.text.split('by')[0].strip()
        # Limpia el título del libro para hacerlo apto como nombre de archivo
        filename = clean_title(book_title) + '.txt'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(book_content)

        print(f'Descargado y guardado: {filename}')
    else:
        print(f'El libro "{book_link.text}" no está disponible en formato Plain text')