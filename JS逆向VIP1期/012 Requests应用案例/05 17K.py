import requests




url = "https://passport.17k.com/ck/user/login"
headers = {
"Host": "passport.17k.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "CONTENT-TYPE": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://passport.17k.com",
    "Referer": "https://passport.17k.com/login/",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "GUID=d7c84636-2d54-4da0-8239-5f5d3861bed9; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22d7c84636-2d54-4da0-8239-5f5d3861bed9%22%2C%22%24device_id%22%3A%22186c17485fa96b-065545e235f8f1-26031951-2073600-186c17485fbc50%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; BAIDU_SSP_lcr=https://www.baidu.com/link?url=jL3xgLo43lNNqcmh5osPphXYtlm9PXJ4Y27OOpO65HG&wd=&eqid=927684e1000010880000000664089076; __bid_n=186c174880ded18b894207; Hm_lvt_9793f42b498361373512340937deb2a0=1678282885; Hm_lpvt_9793f42b498361373512340937deb2a0=1678282885; FPTOKEN=8WoXq3cgScEnkpFpWu2I6fxvrmbLaNTgKGD+ZbJPxawiZLfJzAVo8cfqiNfYtl7Hp8xUUJkSrawJ+tZU8i9j1c0U2zSK7JLgDGiJLAH3OGHzzIY0v0MLV+uSnMgx2B5Our/O5hiYa431mZnleYuKuBCtNHfS98tHlzN9037abbDSbyD/2gNvopzgqF4rXsuzrfj09IpG+qvoABeiI/HTqe/JeV0vNQAb9/3Qcsf7eQdf0hvTNyo4dTXYks0bvvYKNze2cLsqYiYmoxjlzukFOXUqh1qKV/IUQ+vrEdSHY+q4W0yPx/O8CfTI3WF1rowY+ZiOOsvaOZz864M9KCw6M2tbMTqsK81PgBsHJ98ZMGjAZeRJxagZsNJzJWv+WJ+khocTaU9YI37vfZoEhVEQww==|A0+f4q1aYu6zhY7coXT/xmd70R8BZW2I0VJiyrW43sI=|10|f863cc7cc2762fa5f0ff6ad4a3d79eff"
}
datas = {
    "loginName": "17791383347",
    "password": "asd1234"
}
res = requests.post(url, headers=headers, data=datas,proxies={

    "http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888"
},verify=False)
accessToken = res.headers.get("Set-Cookie")
res.headers.get("Cookie")

# 登录
url2 = "https://www.17k.com/"
# Cookie =
header2 = {

}