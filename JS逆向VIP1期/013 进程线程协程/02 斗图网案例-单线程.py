import os.path
import requests
from lxml import etree

url = "https://www.pkdoutu.com/photo/list"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",

}
res = requests.get(url, headers=headers)
# print( res.text)

selector = etree.HTML(res.text)
img_urls = selector.xpath(
    '//div[@class="page-content text-center"]/div/a/img[@referrerpolicy="no-referrer"]/@data-original')


# print(img_urls,len(img_urls))

def download_imgs(img_url):
    res = requests.get(img_url)
    img_name = os.path.basename(img_url)
    path = os.path.join("imgs", img_name)
    with open(path, "wb") as f:
        for i in res.iter_content():
            f.write(i)


for img_url in img_urls:
    download_imgs(img_url)
