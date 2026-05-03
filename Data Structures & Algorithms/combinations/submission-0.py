class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sub = []
        def helper(i, curr, subset):
            if len(curr) == k:
                subset.append(curr.copy())
                return
            if i > n:
                return 
            
            for j in range(i, n+1):
                curr.append(j)
                helper(j+1, curr, subset)
                curr.pop()
        helper(1, [], sub)
        return sub
        