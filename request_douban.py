import requests
from bs4 import BeautifulSoup

content = requests.get('https://book.douban.com/').text
soup = BeautifulSoup(content, 'lxml')

for li in soup.select('.carousel ul li'):
    _elmAuthor = li.select('div.author')
    _elmImag = li.select('div.cover img')


    print(_elmImag[0].attrs['src'].strip(), _elmAuthor[0].get_text().strip())