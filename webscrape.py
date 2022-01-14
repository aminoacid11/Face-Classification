from email import header
import requests, lxml, re, json
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=강아지상+남자"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"id":"imgList"})

print(images)
# for image in images:
#     print(image["data-src"])