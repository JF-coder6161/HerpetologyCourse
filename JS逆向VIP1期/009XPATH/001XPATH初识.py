import requests
from lxml import etree

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50"
}
resp = requests.get(url, headers=headers)

selector = etree.HTML(resp.text)

selectors = selector.xpath('//ol[@class="grid_view"]//li')
print(selectors)
for item in selectors:
    movieName = item.xpath('//span[@class="title"]')[0].text
    print(item)
