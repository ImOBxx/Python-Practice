from bs4 import BeautifulSoup
import requests

with open('WScr.Test.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify()) also print(soup)

match = soup.find('div', class_ = 'footer')
print(match)

article = soup.find('div', class_ = 'footer')
print(article)

for article in soup.find_all('div', class_ = 'footer'):


          headline = article.h2.a.text
          print(headline)

          summary = article.p.text
          print(summary)







