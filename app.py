from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

url = "https://www.businesstoday.in/technology"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
outerData = soup.find_all("div", class_ = "widget-listing", limit=6)
finalnews = ""
for data in outerData:
    news = data.div.div.a["title"]
    finalnews += "\u2022 " + news + "\n"
print(finalnews)
