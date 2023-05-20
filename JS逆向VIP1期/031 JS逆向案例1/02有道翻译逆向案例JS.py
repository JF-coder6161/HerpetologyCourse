import requests
import execjs
import base64

with open('02JS/getRequestParamForEncryptData.js', 'r') as fs:
    jsCode = fs.read()

jsCompileCode = execjs.compile(jsCode)
paramOne = 'fsdsogkndfokasodnaso'

retSomeRequestParam = jsCompileCode.call('getRquestParamForDecodeData',paramOne)

session = requests.session()

word = "apple"

paramDatas = {
    "i": word,
    "from": "auto",
    "to": "",
    "domain": "0",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign":retSomeRequestParam.get('sign') ,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": str(retSomeRequestParam.get('mysticTime')),
    "keyfrom": "fanyi.web",
}
# print(paramDatas)
res = session.post("https://dict.youdao.com/webtranslate", data=paramDatas, headers={
    "Cookie": "OUTFOX_SEARCH_USER_ID=-153512706@10.110.96.158; OUTFOX_SEARCH_USER_ID_NCOO=1470896229.071856"
    , "Referer": "https://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})

encrypt_data = res.text.replace("-", "+").replace("_", "/")
print("encrypt_data:", encrypt_data)

with open('02JS/decryptResposeData.js', 'r') as fs:
    jsCodeDecryptResponseData = fs.read()

jsCompileCodeForDecryptedData = execjs.compile(jsCodeDecryptResponseData)
retDecryptedData = jsCompileCodeForDecryptedData.call('decryptResponseData',encrypt_data)

print(retDecryptedData)

ret = base64.b64decode(retDecryptedData).decode()
print(ret)
