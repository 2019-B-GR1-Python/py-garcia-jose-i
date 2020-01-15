import scrapy
import numpy
from re import sub
from decimal import Decimal

class IntroSpider(scrapy.Spider):
    name = 'introduction_spider'
    urls = ['http://books.toscrape.com/catalogue/category/books_1/index.html']

    def start_requests(self):
        scrapy.Request(self.urls[0])
        for url in self.urls:
            yield scrapy.Request(url)
            

    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        # Ejercicio 0 títulos
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        print(titulos)
        # Ejercicio 1 links de imágenes
        links_to_images = etiqueta_contenedora.css('div > a::attr(href)').extract()
        links = []
        for link in links_to_images:
            links.append(response.urljoin(link))
        print(links)
        # Ejercicio 2 precios
        prices = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        prices_decimal = map(lambda money: Decimal(sub(r'[^\d.]', '', money)), prices)
        print(list(prices_decimal))
