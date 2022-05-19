import requests
from bs4 import BeautifulSoup

PATH = ''
HOST = 'https://knowyourmeme.com'
URL = 'https://knowyourmeme.com/photos/trending/page/1'
HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

num = 1
suoernum = int(input('Сколько мемов спарсить?\n'))
y_n = input("Надо менять путь для расположения мемов?(y/n)\n")

if (y_n == 'y'): PATH = input('Введите путь\n')

def pm(path, url, host, mnum, supernum, _headers=None):
    text = requests.get(url, headers=_headers).text
    soup = B'eautifulSoup(text, features='html.parser')
    
    for i in soup.find_all('div', {'class': ['item']}):
        link =i.find('a').get('href') 
        full = requests.get(host+link, headers=_headers).text
        soup_for_page = BeautifulSoup(full, features='html.parser')
        our_image = soup_for_page.find('img', {'class': ['centered_photo']})
        data_src = our_image.get('data-src')
        if data_src[len(data_src)-4:] != '.gif':
            get_photo = requests.get(data_src)
            with open(path.replace('\\', '\\\\') + '\\' + f'meme{mnum+1}.jpg', 'wb') as code:
                code.write(get_photo.content)
            mnum += 1
        if mnum == supernum: break
    if mnum != supernum:
        new_url =  url.split('/')
        new_url[len(new_url) - 1] = str(int(mnum / 18 + 1))
        pm(path, '/'.join(new_url), host, mnum, supernum)
pm(PATH, URL, HOST, 0, supernum, HEADERS)
