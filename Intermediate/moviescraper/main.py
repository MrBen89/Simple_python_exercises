import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(name="h3", class_="title")

#for article_tag in articles:
#    text = article_tag.getText()
#    article_texts.append(text)
#    link = article_tag.a.get("href")
#    article_links.append(link)

film_list = []
flipped_list = []
for title in titles:
    film = title.getText()
    try:
        film_list.append(film.split(") ")[1])
    except:
        film_list.append(film.split(": ")[1])


for num in range(0,100):
    flipped_list.append(f"{1+num}: {film_list[99-num]}")

print(flipped_list)
