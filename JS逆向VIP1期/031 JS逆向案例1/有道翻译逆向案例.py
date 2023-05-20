import requests
import time
from hashlib import md5

session = requests.session()

word = "apple"
mysticTime = str(int(time.time() * 1000))
print(mysticTime)
oragen_sign = f'client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key=fsdsogkndfokasodnaso'

print(oragen_sign)
m = md5()
m.update(oragen_sign.encode())
sign = m.hexdigest()
print(sign)

# proxy = {'http': 'http://127.0.0.1:8888'}

res = session.post("https://dict.youdao.com/webtranslate", data={
    "i": word,
    "from": "auto",
    "to": "",
    "domain": "0",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": sign,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": mysticTime,
    "keyfrom": "fanyi.web",
}, headers={
    "Cookie": "OUTFOX_SEARCH_USER_ID=-153512706@10.110.96.158; OUTFOX_SEARCH_USER_ID_NCOO=1470896229.071856"
    , "Referer": "https://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})

print(res.text)
