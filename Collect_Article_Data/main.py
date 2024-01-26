from bs4 import BeautifulSoup
import lxml
import requests

URL = "https://news.ycombinator.com/newest"

"""To get the html code of that website"""
response = requests.get(URL)
#print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
article_tag = soup.find(name='span', class_='titleline')
article_text = article_tag.getText()
article_link = soup.find(name='a').get('href')
article_upvote = soup.find(name='span', class_='score').getText()
print(article_text)
print(article_link)
print(article_upvote)
#print(soup.find_all('a'))

# for link in soup.find_all('a'):
#     print(link['href'])
