class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        result = []
        for i in range(len(numbers)):
            if numbers[left] + numbers[right] == target:
                result.append(left+1)
                result.append(right+1)
                return result
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
        return result


            
        