#-*- coding: utf-8 -*-

import sys

import redis


def redisBus(redisip, redisport, redisdb, redispsw):
    pool = redis.ConnectionPool(host = redisip, port = redisport, db = redisdb, password = redispsw)
    return redis.Redis(connection_pool = pool)

        

####################################################################
def test():
    rdb = redisBus('127.0.0.1', 6379, 0, None)

    print 'DB Len:', rdb.dbsize()
    
    print rdb.set('test', 'test')
    print rdb.get('test')

    print rdb.set('test1', 'test1')
    print rdb.set('test2', 'test2')

    print 'DB Len:', rdb.dbsize()
    
    print rdb.delete('test')

    print 'DB Len:', rdb.dbsize()

    ret = rdb.keys('*')
    print ret

    for i in ret:
        print i,':', rdb.get(i)

        
    print rdb.lpush('testlist', 'testlist1')
    print rdb.lpush('testlist', 'testlist2')    
    print rdb.lpush('testlist', 'testlist3')

    pipe = rdb.pipeline()

    i = 0
    while i < 3:
        pipe.rpop('testlist')
        i = i + 1
        
    retlist = pipe.execute()
    print retlist
    
    print rdb.rpop('testlist')
    
    print rdb.flushdb()
    print rdb.flushall()



if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit()


    if sys.argv[1] == 'test':
        test()


    exit()