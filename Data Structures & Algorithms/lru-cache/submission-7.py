import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.mp = OrderedDict()
        self.capacity = capacity
    

    def get(self, key: int) -> int:
        if key in self.mp:
            tmp = self.mp.pop(key)
            self.mp[key] = tmp
        else:
            return -1
        return self.mp[key]
        

    def put(self, key: int, value: int) -> None:
        if len(self.mp) == self.capacity and key not in self.mp:
            self.mp.popitem(last=False)
        if key in self.mp:
            self.mp.pop(key)
        self.mp[key] = value
       

