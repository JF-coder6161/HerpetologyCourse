import requests

#requests.get("",headers={},params={})

res = requests.get("https://www.baidu.com/")
print(type(res)) # <class 'requests.models.Response'>

print(res.status_code)
print(res.headers)
print(res.text) # 字符串  res.text 默认有解码过程
print(res.content) # 字节数据流
print(res.encoding) # ISO-8859-1

with open("baidu.html","w",encoding="ISO-8859-1") as fp:
    fp.write(res.text)
    
with open("baidu1.html","wb") as fp1:
    fp1.write(res.content)
    
