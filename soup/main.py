from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

y_c_webpage = response.text

soup = BeautifulSoup(y_c_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]




index = article_upvotes.index(max(article_upvotes))

print(article_texts[index], article_links[index], article_upvotes[index])
