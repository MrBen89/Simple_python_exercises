from bs4 import BeautifulSoup
import requests

response = requests.get("https://auctions.yahoo.co.jp/closedsearch/closedsearch?p=%E9%AD%94%E7%95%8C%E6%9D%91&auccat=2084005536&va=%E9%AD%94%E7%95%8C%E6%9D%91&b=1&n=50")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
prices = soup.find_all(name="span", class_="Product__priceValue")

#for article_tag in articles:
#    text = article_tag.getText()
#    article_texts.append(text)
#    link = article_tag.a.get("href")
#    article_links.append(link)

price_list = []
for price in prices:
    cost = price.getText()
    price_list.append(cost)
print(price_list)
