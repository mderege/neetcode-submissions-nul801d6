class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        for i in range(len(nums)):
            prefix.append(nums[i]*prefix[-1])
            postfix.append(nums[-i-1]*postfix[-1])
        #postfix = postfix[1:]
        r = []
        
        for i in range(len(prefix)-1):
            r.append(postfix[-i-2]*prefix[i])
        return r
        