class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = {}

        for i in range(len(nums)):
            if nums[i] in other:
                print("here")
                if i < other[nums[i]]:
                    print("here")
                    return [i, other[target-nums[i]]]
                elif i > other[nums[i]]:
                    print("here")
                    return [other[nums[i]], i]
            else:
                other[target-nums[i]] = i
        print(other)
        return []
        