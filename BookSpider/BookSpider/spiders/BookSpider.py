# -*- coding: utf-8 -*-
import scrapy


class BookspiderSpider(scrapy.Spider):
    name = 'BookSpider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # 提取数据
        # 每一本书的信息在<article class="product_pod">中，我们使用
        # css()方法找到所有这样的article 元素，并依次迭代
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield {
                'name': name,
                'price': price,
            }
            print(book);
            # next_url = response.css('ul.pager li.next a::attr(href)')
            # if next_url:
            #    next_url = response.urljoin(next_url)
            #    yield scrapy.Request(next_url, callback=self.parse)
            # pass
