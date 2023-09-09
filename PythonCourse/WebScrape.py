import bs4
import requests 

res = requests.get('https://quotes.toscrape.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.author')

authors = set()
for name in soup.select(".author"):
    print(authors.add(name.text))