from Crypto import Random
from Crypto.PublicKey import RSA

# 伪随机数生成器
random_gen = Random.new().read

# 生成秘钥对实例对象：1024是秘钥的长度
rsa = RSA.generate(1024, random_gen)

# 获取公钥，保存到文件
private_pem = rsa.exportKey()
with open('private.pem', 'wb') as f:
    f.write(private_pem)

# 获取私钥保存到文件
public_pem = rsa.publickey().exportKey()
with open('public.pem', 'wb') as f:
    f.write(public_pem)