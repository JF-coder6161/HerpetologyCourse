print("tool.chinaz.com".replace("china", "japan"))

print("tool.chinaz.com".find("china"))

import re

s = "666.tool.chinaz.com|888"

ret = re.findall("china",s)


ret = re.findall("[a,b,c,d]","a,b,c,d")

ret = re.findall("[1-9]","0,1,2,3,4")

print(ret)

# part 2 重复 * + ? {}
# +  1到多次 (默认贪婪匹配)
# *  0到多次
# ？ [0,1] 范围重复
# {} {m,n}
ret2 = re.findall("\d+","a,b,234,d,6,888") # ['234', '6', '888']
print(ret2)

ret2 = re.findall("\d*","a,b,234,d,6,888") # 空值 可以匹配上\w的零次匹配
print(ret2)

# 取消贪婪匹配  在重复元字符加一个？ 即取消贪婪匹配
ret2 = re.findall("\d+?","a,b,234,d,6,888");
print(ret2)

ret2 = re.findall("abc*","abc,abccc,abe,ab")  # ['abc', 'abccc', 'ab', 'ab']
ret2 = re.findall("abc*?","abc,abccc,abe,ab")  # ['ab', 'ab', 'ab', 'ab']
print(ret2)

ret2 = re.findall("\w{6}","apple,banana,orange,melon") # ['banana', 'orange']
print(ret2)

ret2 = re.findall("abc?","abc,abccc,abe,ab")  # ['abc', 'abc', 'ab', 'ab']
print(ret2)
ret2 = re.findall("abc??","abc,abccc,abe,ab")  # ['ab', 'ab', 'ab', 'ab']
print(ret2)

# part3: 位置元字符 -> $ ^
# ^ 匹配开始位置
# $ 匹配结束位置
ret3 = re.findall("\d+","123,apple,11") # ['123', '11']
print(ret3)
ret3 = re.findall("^\d+","123,apple,11") # ['123']
print(ret3)
ret3 = re.findall("^\d+","app,123,apple,11") # []
print(ret3)
ret3 = re.findall("\d+$","app,123,apple,11") # ['11']
print(ret3)

# part4 :
# / 管道符 指定原子或正则模式进行二选一或多选一
# () 具备模式捕捉的能力，也就是优先提取数据的能力，通过(?:) 可以取消模式捕获

ret4 = re.findall("\w{5}",",apple,banbna,peach,orange,melon,")

print(ret4)

ret4 = re.findall(",\w{5},",",apple,banbna,peach,orange,melon,") # [',apple,', ',peach,', ',melon,']
print(ret4)

ret4 = re.findall(",(\w{5}),",",apple,banbna,peach,orange,melon,") # ['apple', 'peach', 'melon']
print(ret4)

ret4 = re.findall(",(?:\w{5}),",",apple,banbna,peach,orange,melon,") # ['apple', 'peach', 'melon']
print(ret4)

ret4 = re.findall("\w+@(163|qq).com","123abc@163.com....xsz@qq.com...34s@hotmail.com..") # ['163', 'qq']
print(ret4)
ret4 = re.findall("\w+@(?:163|qq).com","123abc@163.com....xsz@qq.com...34s@hotmail.com..") # ['123abc@163.com', 'xsz@qq.com']
print(ret4)


# part5: 转义符 -> \d \D \w \W \n \s \S \b \B
# 转义的两个功能：
#   1. 将一些普通的符号赋予特殊功能 \d -> [0-9] \D -> [^0-9] \w [0-9a-zA-Z] \W -> [^0-9a-zA-Z]
#   2. 将特殊符号(元字符)取消其特殊功能 \* \. \+ \?

""" \b 一个单词边界原子"""
txt = "my name is nana. nihao,nana"
# r 原生字符串 传入 不需python解释器转义
ret = re.findall(r"\bna\w+",txt) # ['name', 'nana', 'nana']
print(ret)



