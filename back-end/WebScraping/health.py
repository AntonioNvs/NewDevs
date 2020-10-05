from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def health():
    url = 'https://g1.globo.com/ciencia-e-saude/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    req = Request(url, headers=headers)

    site = urlopen(req)

    soup = BeautifulSoup(site, 'html.parser')
    all_news = soup.findAll(attrs={'class': 'feed-post-body'})

    result = []

    for news in all_news:
        a = news.find('a')
        img = news.findAll('img')
        description = news.find(attrs={'class': 'feed-post-body-resumo'}).text

        dictionaty = {
            'title': a.text,
            'url':  a['href'] if a.has_attr('href') else '',
            'img': img[-1]['src'] if img != [] else '',
            'description': description
        }

        result.append(dictionaty)
    return result

if __name__ == "__main__":
    health()