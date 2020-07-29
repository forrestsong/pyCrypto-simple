import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


msg = "待加密明文内容"

# 读取文件中的公钥
key = open('public.pem').read()
publickey = RSA.importKey(key)
# 进行加密
pk = PKCS1_v1_5.new(publickey)
encrypt_text = pk.encrypt(msg.encode())
# 加密通过base64进行编码
result = base64.b64encode(encrypt_text)
with open('CipherMessage.txt', 'wb') as f:
    f.write(result)
print(result)