import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
# 密文
msg=open('CipherMessage.txt').read()

# base64解码
msg = base64.b64decode(msg)
# 获取私钥
privatekey = open('private.pem').read()
rsakey = RSA.importKey(privatekey)
# 进行解密
cipher = PKCS1_v1_5.new(rsakey)
text = cipher.decrypt(msg, 'DecryptError')
# 解密出来的是字节码格式，decodee转换为字符串

print(text.decode())
