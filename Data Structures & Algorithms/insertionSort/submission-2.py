# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        re = []
        re.append(pairs.copy())
        if not pairs:
            return []
        for i in range(1, len(pairs)):
            j = i-1
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                tmp = pairs[j]
                pairs[j] =pairs[j+1]
                pairs[j+1] = tmp
                j -= 1 
            re.append(pairs.copy())
        return re