import re

res = re.findall(r"\d+", "apple 122 peach 34")
print(res)  # ['122', '34']
res = re.search(r"\d+", "apple 122 peach 34")
print(res)  # <re.Match object; span=(6, 9), match='122'>
print(res.group())  # 122

# 有名分组
reg = "(?P<tel>1[3-9]\d{9}).*?(?P<email>\d+@qq.com)"

# match 从开始匹配

reg = "1[3-9]\d{9}"



# split
txt = "my name     is   yuan"
res = re.split(r"\s+", txt)
print(res)

# sub/subn 替换  count  替换次数

txt = "12 34 56 88"
res = re.sub(r"\d+", "haha", txt,2)
print(res) # haha haha 56 88

# compile 编译 省去了编译规则的事件 (多个字符串匹配相同的规则)

s1 = "12 apple 34 peach 77 banana"
res = re.findall(r"\d+",s1)
print(res)

s2 = "22 apple 33 peach"

reg = re.compile(r"\d+")
res = reg.findall(s1)
print(res)
res = reg.findall(s2)
print(res)

# 补充 raw-string : 原生字符串
# yuan316.com
