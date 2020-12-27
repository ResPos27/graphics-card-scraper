import requests
from bs4 import BeautifulSoup

results = []
siteItem = ""

def connectToNewLink(products):
    counter = 0
    for link in products:
        counter += 1
        request = requests.get(link)
        soup = BeautifulSoup(request.text, features="html.parser")
        if (soup.find_all("li", {"class": "nostock"}) == []):
            name = soup.find("h1", {"class": "page-title nosp"})
            price = soup.find("div", {"class": "amounts"})
            results.append([name.span.text, price.text.strip(), link])


request = requests.get(siteItem)
soup = BeautifulSoup(request.text, features="html.parser")
products = []
for product in soup.find_all(class_="productTitle"):
    for link in product("a"):
        products.append(link.get("href"))
connectToNewLink(products)

print(results)
