from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cacheCapacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache.pop(key) 
            self.cache[key] = value
            return value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key) 
        elif len(self.cache) == self.cacheCapacity:
            self.cache.popitem(last=False)
        
        self.cache[key] = value


capacity = 10
key = 1, value = 1024
obj = LRUCache(capacity)
val = obj.get(key)
obj.put(key,value)


