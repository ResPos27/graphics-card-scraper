import sys
import asyncio
import aiohttp
import itertools
from bs4 import BeautifulSoup

print(str(sys.argv))


async def connect_to_primary_links(session, url):
    async with session.get(url) as response:
        text = await response.text()
        sub_links = await extract_sub_links(text)
        return sub_links


async def extract_sub_links(text):
    try:
        soup = BeautifulSoup(text, features="html.parser")
        products = []
        for product in soup.find_all(class_="productTitle"):
            for link in product("a"):
                products.append(link.get("href"))
        return products
    except Excetion as e:
        return str(e)


async def connect_to_sublinks(session, url):
    async with session.get(url) as response:
        text = await response.text()
        products = await extract_product_info(text, url)
        return products


async def extract_product_info(text, url):
    results = []
    try:
        soup = BeautifulSoup(text, features="html.parser")
        if (soup.find_all("li", {"class": "nostock"}) == []):
            name = soup.find("h1", {"class": "page-title nosp"})
            price = soup.find("div", {"class": "amounts"})
            results.append([name.span.text, price.text.strip(), url])
        return results
    except Exception as e:
        results.append(str(e))


async def main(loop):
    urls = ['https://www.currys.co.uk/gbuk/search-keywords/xx_xx_30343_xx_xx/3060/xx-criteria.html']
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [connect_to_primary_links(session, url) for url in urls]
        subLinks = await asyncio.gather(*tasks)
        subLinks = list(itertools.chain.from_iterable(subLinks))
        subtasks = [connect_to_sublinks(session, url) for url in subLinks]
        products = await asyncio.gather(*subtasks)
        print(products)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
