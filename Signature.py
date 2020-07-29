from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk
from Crypto.PublicKey import RSA
import base64

# 待签名内容
name = "ScottSong"
# 获取私钥
key = open('private.pem', 'r').read()
rsakey = RSA.importKey(key)
# 根据sha算法处理签名内容  (此处的hash算法不一定是sha,看开发)
data = SHA.new(name.encode())
# 私钥进行签名
sig_pk = Sig_pk.new(rsakey)
sign = sig_pk.sign(data)
# 将签名后的内容，转换为base64编码
result = base64.b64encode(sign)
# 签名结果转换成字符串
data = result.decode()
with open('Signed.txt', 'wb') as f:
    f.write(result)
print(data)
