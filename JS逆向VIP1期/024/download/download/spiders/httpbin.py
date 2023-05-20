import scrapy


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["xxx.com"]
    start_urls = ["http://httpbin.org/get"]

    def parse(self, response):
        print("response:::",response.text)
