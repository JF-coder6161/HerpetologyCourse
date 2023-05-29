import requests
import time
import execjs

with open('./getCookie.js', "r") as fs:
    jsCode = fs.read()

jsCodeCompile = execjs.compile(jsCode)

partOfCookies = jsCodeCompile.call("getCookie")

cookie = f'other_uid=Ths_iwencai_Xuangu_ouy56jc53f7npcxj40yqzu4ierowfttx; ta_random_userid=fm6hqlr3ub; cid=ca3d3615df29f226d32385a01af41cb61684845024; v={partOfCookies}'
hexinValue = partOfCookies
requestUrl = 'http://www.iwencai.com/customized/chart/get-robot-data'
request_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": 'no-cache',
    "Content-Length": "360",
    "Content-Type": "application/json",
    "Cookie": cookie,
    "Hexin-V": hexinValue,
    "Host": "www.iwencai.com",
    "Origin": "http://www.iwencai.com",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Referer": f"http://www.iwencai.com/unifiedwap/result?w=%E4%BB%8A%E6%97%A5%E6%B6%A8%E5%81%9C&querytype=stock&addSign={int(time.time() * 10000)}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# print(request_headers)

jsonData = {
    "source": "Ths_iwencai_Xuangu",
    "version": "2.0",
    "query_area": "",
    "block_list": "",
    "add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
    "question": "今日涨停",
    "perpage": 50,
    "page": 1,
    "secondary_intent": "stock",
    "log_info": "{\"input_type\":\"typewrite\"}",
    "rsh": "Ths_iwencai_Xuangu_ouy56jc53f7npcxj40yqzu4ierowfttx"
}

response = requests.post(url=requestUrl, headers=request_headers, json=jsonData)
print(response.text)
