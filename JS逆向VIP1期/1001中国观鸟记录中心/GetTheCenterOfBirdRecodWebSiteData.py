import requests
import execjs
import json

with open("./JS/getRequestHeaders.js", "r", encoding='utf-8') as fp:
    jsCode = fp.read()
jsCompile = execjs.compile(jsCode)
requestsParam = jsCompile.call("getRequestHeaders", 'page=1&limit=20')
requestsParamJson = json.loads(requestsParam)
print(requestsParamJson)

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
    "Requestid": requestsParamJson.get("requestId"),
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": '?0',
    "Sec-Ch-Ua-Platform": 'Windows',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sign": requestsParamJson.get("sign"),
    "Timestamp": str(requestsParamJson.get("timestamp")),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

requestData = requestsParamJson.get("data")

response = requests.post(url=requestUrl, headers=requestHeaders, data=requestData)
responseDataJson = json.loads(response.text)
print("data:::", responseDataJson.get("data"))
with open("./JS/parseResponseData.js", "r", encoding='utf-8') as fpp:
    jsParseCode = fpp.read()
jsParseCodeCompile = execjs.compile(jsParseCode)
responseParseData = jsParseCodeCompile.call("getParseData", responseDataJson.get("data"))

print(type(responseParseData))
print(responseParseData)
