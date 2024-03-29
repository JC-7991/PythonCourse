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

url = 'http://quotes.scrape.com/page/'
authors = set()

for page in range(1, 10):

    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select(".author"):
        authors.add(name.text)

print(authors)