import scrapy


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    allowed_domains = ["news.163.com"]
    # 起始地址
    start_urls = ["http://news.163.com/"]

    # 解析方法(回调函数)
    def parse(self, response):
        with open("news163.html","w") as f:
            f.write(response.text)

