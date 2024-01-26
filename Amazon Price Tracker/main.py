import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

email = "abc@gmail.com"
password = "pswd"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url_addr = 'https://www.amazon.com/Apple-iPhone-Plus-128-trade/dp/B0CHBPTX1P/ref=sxin_9_hcs-iphone-pl-us-1?content-id=amzn1.sym.75113e5d-efff-49ae-bba9-d45d69f2eefc%3Aamzn1.sym.75113e5d-efff-49ae-bba9-d45d69f2eefc&crid=2OPPH4Q1KGJLZ&cv_ct_cx=iphone+15+pro+max&dib=eyJ2IjoiMSJ9.mkVwt1leAIWwm7eXPZKnwBipfbqLQGvzK8viyhIvuguOLaFIB9S-77bJkyElM615.wqXOKnsY41VAQarGnZWkGmrExccuAfi_g4KWM4G7KCk&dib_tag=se&keywords=iphone+15+pro+max&pd_rd_i=B0CHBPTX1P&pd_rd_r=0caf3a2e-c60a-4718-a581-dda16b71774e&pd_rd_w=giRmB&pd_rd_wg=Bzi5G&pf_rd_p=75113e5d-efff-49ae-bba9-d45d69f2eefc&pf_rd_r=9C5DKKPV97QR9WMWGGS8&qid=1705119769&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=iphone+15+pro+max%2Caps%2C94&sr=1-3-acced174-0150-4fc5-bcd1-b989ebc3c57d'

html_doc = requests.get(url=url_addr, headers=header)
soup = BeautifulSoup(html_doc.content, "lxml")
value = soup.find(name="span", class_="a-offscreen").get_text()
value = value.split('$')
"main.py" 28L, 1702B
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

email = "v82726794@gmail.com"
password = "exjm vqhn hftn geav"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url_addr = 'https://www.amazon.com/Apple-iPhone-Plus-128-trade/dp/B0CHBPTX1P/ref=sxin_9_hcs-iphone-pl-us-1?content-id=amzn1.sym.75113e5d-efff-49ae-bba9-d45d69f2eefc%3Aamzn1.sym.75113e5d-efff-49ae-bba9-d45d69f2eefc&crid=2OPPH4Q1KGJLZ&cv_ct_cx=iphone+15+pro+max&dib=eyJ2IjoiMSJ9.mkVwt1leAIWwm7eXPZKnwBipfbqLQGvzK8viyhIvuguOLaFIB9S-77bJkyElM615.wqXOKnsY41VAQarGnZWkGmrExccuAfi_g4KWM4G7KCk&dib_tag=se&keywords=iphone+15+pro+max&pd_rd_i=B0CHBPTX1P&pd_rd_r=0caf3a2e-c60a-4718-a581-dda16b71774e&pd_rd_w=giRmB&pd_rd_wg=Bzi5G&pf_rd_p=75113e5d-efff-49ae-bba9-d45d69f2eefc&pf_rd_r=9C5DKKPV97QR9WMWGGS8&qid=1705119769&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=iphone+15+pro+max%2Caps%2C94&sr=1-3-acced174-0150-4fc5-bcd1-b989ebc3c57d'

html_doc = requests.get(url=url_addr, headers=header)
soup = BeautifulSoup(html_doc.content, "lxml")
value = soup.find(name="span", class_="a-offscreen").get_text()
value = value.split('$')
"main.py" 28L, 1702B
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

email = "v82726794@gmail.com"
password = "exjm vqhn hftn geav"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url_addr = 'https://www.amazon.com/Apple-iPhone-Plus-128-trade/dp/B0CHBPTX1P/ref=sxin_9_hcs-iphone-pl-us-1?content-id=amzn1.sym.75113e5d-efff-49ae-bba9-d45d69f2eefc%3Aamzn1.sym.75113e5d-efff-49ae-bba9-d45d69f2eefc&crid=2OPPH4Q1KGJLZ&cv_ct_cx=iphone+15+pro+max&dib=eyJ2IjoiMSJ9.mkVwt1leAIWwm7eXPZKnwBipfbqLQGvzK8viyhIvuguOLaFIB9S-77bJkyElM615.wqXOKnsY41VAQarGnZWkGmrExccuAfi_g4KWM4G7KCk&dib_tag=se&keywords=iphone+15+pro+max&pd_rd_i=B0CHBPTX1P&pd_rd_r=0caf3a2e-c60a-4718-a581-dda16b71774e&pd_rd_w=giRmB&pd_rd_wg=Bzi5G&pf_rd_p=75113e5d-efff-49ae-bba9-d45d69f2eefc&pf_rd_r=9C5DKKPV97QR9WMWGGS8&qid=1705119769&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=iphone+15+pro+max%2Caps%2C94&sr=1-3-acced174-0150-4fc5-bcd1-b989ebc3c57d'

html_doc = requests.get(url=url_addr, headers=header)
soup = BeautifulSoup(html_doc.content, "lxml")
value = soup.find(name="span", class_="a-offscreen").get_text()
value = value.split('$')
price = round(float(value[1]))

message = f"The price of iphone15 pro is {price} and here is a website link\n{url_addr}"
if price < 800:
    with SMTP("smtp.gmail.com") as connection:


