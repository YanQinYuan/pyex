#第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
#coding=utf-8
from hashlib import sha256
import hmac

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


import random

def set_password(raw_password, salt):#是否加盐
    # if salt is None:
    #     salt = sha256(str(random.random())).hexdigest()[-8:]
    # if isinstance(raw_password, unicode):
    #     raw_password = raw_password.encode('utf-8')
    # password = HMAC(salt,raw_password,sha256).hexdigest()
    # return ('%s$%s'%(salt,password))
    return hmac.new(raw_password, salt, digestmod='MD5').hexdigest()


def check_password(raw_password,salt,enc_password):
    return enc_password == set_password(raw_password,salt)



if __name__ == '__main__':
    raw_password1 = b'hehe'
    raw_password2 = b'test'
    salt = b'2324'
    enc_password1 = set_password(raw_password1,salt)
    enc_password2 = set_password(raw_password2, salt)
    print('enc1:%s' % enc_password1)
    print('enc2:%s' % enc_password2)
    print(check_password(raw_password1,salt,enc_password1))
    print(check_password(raw_password2,salt,enc_password2))
    
