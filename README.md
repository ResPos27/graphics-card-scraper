# Async Currys web scraper
This program is designed to work on the Currys UK website to automatically visit each search item provided in a URL and output whether the product in question is in stock. If the product is in stock, the manufacturer, price and URL to that product will be printed out. This program uses asynchronous operation to speed up getting results.

## Getting Started
Install the dependencies, which can be found in [requirements.txt](../main/requirements.txt).

### Prerequisites
```pip install -r requirements.txt```

### Technologies
Python 3.8.6

[BeautifulSoup 4.9.3](https://pypi.org/project/beautifulsoup4/)

[Aiohttp](https://pypi.org/project/aiohttp/)

Asyncio, part of the standard Python library since version 3.4.

### Docker
* Install Docker 
* Build the Docker image:

`docker build -t webscraper .`

* Run the Docker image

`docker run webscraper`

## License
This project is licensed under the MIT License - see the [LICENSE.md](../main/LICENSE) for details.
