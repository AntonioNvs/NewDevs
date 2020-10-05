from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def politics():
    url = 'https://g1.globo.com/politica/'
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
        img = img[-1]

        descrip = news.find(attrs={'class': 'feed-post-body-resumo'})

        description = descrip.text if descrip is not None else ''


        dictionaty = {
            'title': a.text,
            'url':  a['href'] if a.has_attr('href') else '',
            'img': img['src'],
            'description': description
        }

        result.append(dictionaty)
    
    return result

if __name__ == "__main__":
    politics()