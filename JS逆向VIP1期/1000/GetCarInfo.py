import requests
from urllib import parse
import json

encodedData = {"cityId": "2301", "serialId": "1729"}

encodedDataJson = json.dumps(encodedData, separators=(',', ':'))

encodedParam = parse.quote(encodedDataJson)

print("encodedParam", encodedParam)

requestUrl = f'https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param={encodedParam}'

response = requests.get(url=requestUrl)


# https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param=%7B%22cityId%22%3A%222301%22%2C%22serialId%22%3A%221729%22%7D
# https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param=%7B%22cityId%22%3A%222301%22%2C%22serialId%22%3A%221729%22%7D

str = parse.unquote('%257B%2522serialId%2522%253A1729%257D')
print(str)
