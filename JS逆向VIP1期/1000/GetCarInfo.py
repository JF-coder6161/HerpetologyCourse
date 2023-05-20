import time
from hashlib import md5
import requests
from urllib import parse
import json

cityId = "2301"
serialId = "2573"
currentTime = int(time.time()*1000)
encodedData = {"cityId": cityId, "serialId": serialId}

encodedDataJson = json.dumps(encodedData, separators=(',', ':'))

encodedParam = parse.quote(encodedDataJson)

print("encodedParam", encodedParam)

requestUrl = f'https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param={encodedParam}'
baseSign = f'cid=508&param={encodedDataJson}19DDD1FBDFF065D3A4DA777D2D7A81EC{currentTime}'
# print("baseSign::" ,baseSign)
obj = md5()
obj.update(baseSign.encode())
xSign = obj.hexdigest()
# print("encryptedSign::",xSign,type(xSign))
xIpAddress = "222.90.64.153"
xPlatform = "pc"
xUserGuid = "824381ad-2e9d-4be6-be95-7ac32d600230"

requestHeader = {
    "Content-Type": 'application/json;charset=UTF-8',
    "Cookie": 'CIGUID=824381ad-2e9d-4be6-be95-7ac32d600230; auto_id=7ceadc4bb94c34a5aaa61da74f9c75fd; CIGDCID=5FPsJnZRhHNwwhKb8t4cpFmhaNNGMBBD; UserGuid=824381ad-2e9d-4be6-be95-7ac32d600230; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1684501064; selectcity=610100; selectcityid=2301; selectcityName=%E8%A5%BF%E5%AE%89; isWebP=true; locatecity=610100; bitauto_ipregion=222.90.64.153%3A%E9%99%95%E8%A5%BF%E7%9C%81%E8%A5%BF%E5%AE%89%E5%B8%82%3B2301%2C%E8%A5%BF%E5%AE%89%E5%B8%82%2Cxian; csids=2573_1729; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1684587659',
    "Referer": 'https://car.yiche.com/xinaodia6l/peizhi/',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    "X-City-Id": cityId,
    "X-Ip-Address": xIpAddress,
    "X-Platform": xPlatform,
    "X-Sign": xSign,
    "X-Timestamp": str(currentTime),
    "X-User-Guid": xUserGuid,
}

response = requests.get(url=requestUrl,headers=requestHeader)
print(response.text)
