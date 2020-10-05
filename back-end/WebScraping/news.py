import requests

def news():
    url = ('http://newsapi.org/v2/top-headlines?'
        'country=br&'
        'apiKey=85c4ccf422ea4aadb1ad4f767591b721')
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    news()