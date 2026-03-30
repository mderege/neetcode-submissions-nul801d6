# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.quickS(pairs, 0, len(pairs)-1)
    
    def quickS(self, arr, s , e):
        if e-s+1 <= 1:
            return arr

        left = s+(e-s//2)
        curr = s
        for i in range(s, e):
            if arr[i].key < arr[e].key:
                tmp = arr[curr]
                arr[curr] = arr[i] 
                arr[i] = tmp
                curr +=1
        tmp = arr[curr]
        arr[curr] = arr[e]
        arr[e] = tmp

        self.quickS(arr, s, curr-1)
        self.quickS(arr, curr+1, e)

        return arr

