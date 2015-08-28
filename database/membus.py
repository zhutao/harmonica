#-*- coding: utf-8 -*-

import sys

import memcache

MEMCACHEDB = ['127.0.0.1:11211']

class MemBus:
    '''
    This class for memcache API
    '''
    def __init__(self):
        self.mc = memcache.Client(MEMCACHEDB, debug = 0)


    def get(self, key):
        ''' REEOR return None '''
        return self.mc.get(key)
        

    def gets(self, keys, key_prefix = ''):
        ''' REEOR return [] '''
        return self.mc.get_multi(keys, key_prefix)
        

    def set(self, key, value, time = 0):
        ''' ERROR return False '''
        return self.mc.set(key, value, time)

        
    def sets(self, mapping, time = 0, key_prefix = ''):
        return self.mc.set_multi(mapping, time, key_prefix)


    def delete(self, key, time = 0):
        ''' ERROR return 0 '''
        return self.mc.delete(key, time)

        


#########################################################################
def test():
    memdb = MemBus()
    
    print memdb.set('test', 'test')
    print memdb.get('test')
    print memdb.delete('test')

    print memdb.sets({'test1': 'test1', 'test2': 'test2'})
    print memdb.gets(['test1', 'test2'])
    print memdb.delete('test1')
    print memdb.delete('test2')

    
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit()

    if sys.argv[1] == 'test':
        test()

    exit()