import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

TARGET_PRICE = 100
URL = "https://www.amazon.com/dp/B0B727YMJT/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price = soup.find(name="span", class_="a-price-whole").text

print(price)

if price < TARGET_PRICE:
    with SMTP("smtp-mail.outlook.com", port=587) as connection:
         connection.starttls()
         connection.login(user= "EMAIL", password= "PASSWORD")
         connection.sendmail(
             from_addr="FROM",
             to_addrs="TO",
             msg=f"Hi!\n\n{URL} {price}"
         )
