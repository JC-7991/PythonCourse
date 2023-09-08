import bs4
import requests 

res = requests.get('https://quotes.toscrape.com')
#print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')