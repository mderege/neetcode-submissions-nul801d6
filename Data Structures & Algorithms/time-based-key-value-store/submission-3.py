class TimeMap:

    def __init__(self):
        self.feelDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr = []
        curr.append(timestamp)
        curr.append(value)
        if key in self.feelDict.keys():
            self.feelDict[key].append(curr) 
        else:
            self.feelDict[key] = []
            self.feelDict[key].append(curr)
        
        curr = []

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.feelDict:
            return ""
        currList = self.feelDict[key]

        l = 0 
        r = len(currList)-1
        result = ""
        while l <= r:

            m = l + (r-l)//2
            print(currList)
            if currList[m][0] <= timestamp:
                result = currList[m][1]
                l = m+1
            else:
                r = m-1

        return result

        
