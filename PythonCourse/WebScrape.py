import bs4
import requests 

res = requests.get('https://quotes.toscrape.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.author')

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)

url = 'https://quotes.scrape.com/page/'