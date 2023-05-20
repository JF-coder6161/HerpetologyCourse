import requests
import execjs
import json

with open('GetRequestParam.js', 'r') as fs:
    jsCode = fs.read()

jsCompileCode = execjs.compile(jsCode)

id = 500665346
idChange = f'[{id}]'
paramOneFlexible = {"ids": idChange, "level": "standard", "encodeType": "aac", "csrf_token": ""}
paramOneFlexibleStr = str(paramOneFlexible)
paramTwoFixed = '010001'
paramThreeFixed = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7';
paramFourFixed = '0CoJUm6Qyw8W8jud'

ret = jsCompileCode.call('getRequestParam', paramOneFlexibleStr, paramTwoFixed, paramThreeFixed, paramFourFixed)

url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='

data = {
    "params": ret['encText'],
    "encSecKey": ret['encSecKey']
}

print("data",data)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    , 'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url,data=data,headers=header)
# print("response::",response.json())
responseJson = response.json()
# print(type(responseJson))
url = responseJson.get('data')[0].get('url')
# print("url::",url)

responseMusicData = requests.get(url)

with open('平凡之路.m4a','wb') as fsMusic:
    fsMusic.write(responseMusicData.content)





