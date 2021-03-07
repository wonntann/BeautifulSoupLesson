from bs4 import BeautifulSoup
import requests

# Installing BeautifulSoup via pip directions
# source = requests.get('https://pypi.org/project/beautifulsoup4/').text

# Beautiful Soup documentation
source = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/').text

soup = BeautifulSoup(source, 'lxml')

page = soup.find('div', class_='body')
# print(page)
title = soup.select('div.section ~ p')
print(title)

# Definition
paragraph = soup.find('p').text
print(paragraph)

# Main page documentation
# find main beautiful soup documentation
# Directions
# Using the id argument
headline = soup.find('div', id='installing-beautiful-soup').h1.text
print(headline)

# Blank line after each loop
print()
