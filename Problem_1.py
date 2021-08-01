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
print(our_cache.cache) # returns {1: 1, 2: 2, 3: 3, 4: 4}

our_cache.set('','')
our_cache.set(None,None) 
our_cache.set(5e50,5e50)
print(our_cache.cache) # returns {3: 3, 4: 4, '': '', None: None, 5e+50: 5e+50}

print(our_cache.get(1))  # returns -1 because the cache reached it's capacity
print(our_cache.get(3)) # returns 3
print(our_cache.get(9)) # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.cache)
our_cache.get(3) # returns 3 because 3 was called by get and is not the least used entry

