import base64

# 编码
# 字符串 (编码) 二进制
encode_data = "you".encode(encoding='utf-8')
print(encode_data)

# Encode the bytes-like object s using Base64 and return a bytes object

altchars = '*'

res = base64.b64encode(encode_data, altchars=altchars.encode())

print(res)  # b'eW91'

print(res.decode())  # eW91

# 解码
# Decode the Base64 encoded bytes-like object or ASCII string s.
# The result is returned as a bytes object.
decode_data = base64.b64decode(res)
print(decode_data)
