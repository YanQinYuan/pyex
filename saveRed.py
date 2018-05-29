#coding=utf-8

import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import gen-num

def saveRed(data):
    # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    for i in data:
        r.set('acNum', i)     # key是"gender" value是"male" 将键值对存入redis缓存

if __name__ == '__main__':
    date = generate(200)
    saveRed(data)


