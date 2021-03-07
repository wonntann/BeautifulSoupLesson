import requests
from bs4 import BeautifulSoup

# pass HTML as string
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
# use keyword class_
# match = soup.find('div', class_='footer')
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()