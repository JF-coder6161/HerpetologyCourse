import scrapy


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    allowed_domains = ["news.163.com"]
    # 起始地址
    start_urls = ["http://news.163.com/"]

    cate_num_map = {
        # "{{__i == 0}}": '要闻',
        # "{{__i == 1}}": '国内',
        # "{{__i == 2}}": '国际',
        # "{{__i == 3}}": '独家',
        # "{{__i == 4}}": '军事',
        # "{{__i == 5}}": '财经',
        "{{__i == 6}}": '科技'
    }

    # 解析方法(回调函数)
    def parse(self, response):
        with open('news.html', "w", encoding='utf-8') as fp:
            fp.write(response.text)

        cate_num_list = response.xpath("//div[contains(@ne-if,'{{')]/@ne-if").extract()
        # list_news_nav1 = []
        # for item in list_news_nav:
        #     newStr = item.strip()
        #     if '' == newStr:
        #         continue
        #     list_news_nav1.append(newStr)


        for cate_num in cate_num_list:
            # 循环每一个板块(类别)
            if cate_num in self.cate_num_map:
                cate_title = self.cate_num_map.get(cate_num)
                news_selector_list = response.xpath(f"//div[contains(@ne-if,'{cate_num}')]//div//a")
                for news_selector in news_selector_list:
                    news_title = news_selector.xpath("text()").extract_first()
                    news_ref = news_selector.xpath("@href").extract_first()
                    print((cate_title,news_title,news_ref))




