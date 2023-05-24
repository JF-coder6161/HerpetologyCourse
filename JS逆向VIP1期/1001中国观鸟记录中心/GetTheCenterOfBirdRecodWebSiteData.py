import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

requestUrl = "https://api.birdreport.cn/front/activity/search"

requestHeaders = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "172",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "api.birdreport.cn",
    "Origin": "http://www.birdreport.cn",
    "Referer": "http://www.birdreport.cn/",
    "Requestid": "88d3c27a0b5bc048510899a05443f7dd",
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": '?0',
    "Sec-Ch-Ua-Platform": 'Windows',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sign": "bd1823aea1b6f219c9b401602e836790",
    "Timestamp": "1684673154000",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
