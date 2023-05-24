from urllib import parse

# 值编码
s = "a=1&b=2"

ret = parse.quote(s)
print("ret::", ret)

# 值解码
ret_1 = parse.unquote(ret)
print("ret::", ret_1)

# 整体数据编码

data = {
    "a": "1&apple",
    "b": "2苑"
}

ret_all = parse.urlencode(data)
print("ret_all::" , ret_all)  # ret_all:: a=1%26apple&b=2%E8%8B%91

decode_ret_all = parse.parse_qs(ret_all)
print("decode_ret_all::",decode_ret_all)


