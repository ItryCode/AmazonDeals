import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

my_email = "smtptrialemail321@gmail.com"
password = "onkaxgxuckcswnlw"
URL="https://www.amazon.in/Mi-Earphone-Basic-Ultra-deep/dp/B07QJYB8BC/ref=sr_1_47?crid=GSEEU8FFQO1T&keywords=earphones%2Bwired&qid=1672060824&sprefix=earphones%2Bwire%2Caps%2C378&sr=8-47&th=1"
headers={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}

response=requests.get(url=URL,headers=headers)
web_page=response.text
amazon=BeautifulSoup(web_page,"lxml")
amazon_prices=amazon.find("span",class_="a-offscreen")
prod_name=amazon.find("span",class_="a-size-large product-title-word-break")
product=prod_name.getText()
price=amazon_prices.getText().split("₹")
curr_price=price[1]
print(curr_price)
if float(curr_price)<500:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="sonuhrajieev@gmail.com",msg=f"{product} price has dropped to {curr_price}")