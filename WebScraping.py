import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site=site
    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html=r.read()
        parser='html.parser'
        sp=BeautifulSoup(html,parser)
        with open('googlenews.txt','w') as f:
            for tag in sp.find_all('a'):
                url=tag.get('href')
                if url is None:
                    continue
                if 'articles/' in url:
                    print('\n'+url)
                    f.write(url+'\n')

Scraper('https://news.google.com/').scrape()