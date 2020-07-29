from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk
from Crypto.PublicKey import RSA
import base64


# 签名之前的内容
name = "ScottSong"

# 签名数据
data=open('Signed.txt').read()
# base64解码
data = base64.b64decode(data)
# 获取公钥
key = open('public.pem').read()
rsakey = RSA.importKey(key)
# 将签名之前的内容进行hash处理
sha_name = SHA.new(name.encode())
# 验证签名
signer = Sig_pk.new(rsakey)
result = signer.verify(sha_name, data)
# 验证通过返回True   不通过返回False
print(data)
print(result)
