import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70",
    "Accept-Language": "en-US,en;q=0.9",

}

URL = "https://www.amazon.com/Precision-Turntable-Cartridge-Belt-Drive-Bluetooth/dp/B083FPMH78/ref=sr_1_18?keywords=gramophone+record+player&pd_rd_r=29d07174-c725-4117-9a47-2e4b20ab0caf&pd_rd_w=UhL39&pd_rd_wg=hbgsf&pf_rd_p=4fa0e97a-13a4-491b-a127-133a554b4da3&pf_rd_r=ZHN8NA7TKM0MW4N5DVTY&qid=1646403684&sr=8-18"

response = requests.get(URL, headers=headers)

page = response.text
#print(page)


soup = BeautifulSoup(page, 'lxml')


product_price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))

if product_price < 100:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Gramophone na popustu! ${product_price}\n\n{URL}"
        )
