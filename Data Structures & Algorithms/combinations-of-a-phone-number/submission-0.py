class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def helper(i, curr, subset):
            if i >= len(digits):
                if curr != "":
                    subset.append(curr)
                return
            
            for j in d[digits[i]]:
                curr = curr+j
                helper(i+1, curr, subset)
                curr = curr[:len(curr)-1]
        subset = []
        helper(0, "", subset)
        return subset
        