class TimeMap:

    def __init__(self):
        self.values = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            self.values[key].append((timestamp, value))
        else:
            self.values[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.values:
            l = 0
            r = len(self.values[key])-1
            mid = 0
            res = ""
            while l <= r:
                mid = ((r-l)//2)+l

                if self.values[key][mid][0] > timestamp:
                    r = mid-1
                elif self.values[key][mid][0] < timestamp:
                    res = self.values[key][mid][1]
                    l = mid+1
                else:
                    return self.values[key][mid][1] 
            return res
        else:
            return ""

