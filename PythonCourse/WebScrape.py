import bs4
import requests 

res = requests.get('https://quotes.toscrape.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.author')

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

soup.select('.text')