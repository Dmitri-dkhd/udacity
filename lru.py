class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()

    
    def get(self, key): # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            item = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = item
            return item
        else:
            return -1

    
    def set(self, key, value): # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache) == self.capacity:
            least_used = next(iter(self.cache))
            self.cache.pop(least_used)
        self.cache[key] = value


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.get(1)
# returns 1
our_cache.get(2)
# returns 2
our_cache.get(9)
# returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.get(3)
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
