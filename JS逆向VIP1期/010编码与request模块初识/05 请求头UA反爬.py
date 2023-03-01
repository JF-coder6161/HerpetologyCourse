import requests

url = "https://www.baidu.com"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

resp = requests.get(url,headers=header)

with open("baidu2.html","wb") as fp:
    fp.write(resp.content)