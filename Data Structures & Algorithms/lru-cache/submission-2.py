class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if key not in self.cache:
                self.cache[key] = value
                self.cache.move_to_end(key)
                self.cache.pop(next(iter(self.cache.keys())))
            else:
                self.cache[key] = value
                self.cache.move_to_end(key)


        
