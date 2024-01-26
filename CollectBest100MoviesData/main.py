from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

html_code = requests.get(URL)

soup = BeautifulSoup(html_code.text, 'html.parser')
movie_list = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__BfenH')
movie_name = []

for link in movie_list:
    name = link.getText()
    movie_name.append(name + '\n')
movies = movie_name[::-1]
with open('movies.txt', 'w') as file:
    for i in range(len(movies)-1):
        file.write(movies[i])
