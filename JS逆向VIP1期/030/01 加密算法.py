from Crypto.Cipher import AES
import base64

# key 的长度是有限制的
key = 'alex is dsb!!!!!'.encode()  # 16长度的字节串

aes = AES.new(key, AES.MODE_ECB)

data = 'hello Jack , you are most powerful man in the world!!'.encode()

while len(data) % 16 != 0:
    data += b"\0"

# 加密数据
en_data = aes.encrypt(data)
print(en_data)
# base64 编码
final_data = base64.b64encode(en_data)
print(final_data)
print(final_data.decode())

# base64解码

decode_data = base64.b64decode('AMVfIBXx0WKlD2WjMZ5bwc64zTRZJRr0C9EA7Fg6yWyVnAYlv6x3v7+Dg9uBOvxnF0Mf45DOfbVtv55riURuXA=='.encode())

print(decode_data)
plain_data = aes.decrypt(key, decode_data)

print(plain_data)
