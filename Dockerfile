FROM python:3.8.6

COPY . /web-scraper

WORKDIR /web-scraper

RUN python3.8 -m pip install aiohttp beautifulsoup4

EXPOSE 80
EXPOSE 443

CMD ["python3.8", "./Web Scraper Async.py"]
