import requests

url = "https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories={}&uncollect=false&tags="

header = {
    "Referer": "https://movie.douban.com/explore",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=header)

print(res.content)
print(res.text)
print(res.content.decode("utf8"))
print(res.json())

# print(res.content.decode("utf8"))

for item in res.json()["items"]:
    if item.get("title"):
        print(item.get("title"))