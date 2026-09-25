class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        fast = len(numbers)-1
        slow = 0

        while slow < fast and slow >= 0 and fast < len(numbers): 
            if numbers[slow]+numbers[fast] == target:
                return [slow+1, fast+1]
            elif numbers[slow]+numbers[fast] < target:
                slow +=1
            else:
                fast -=1
            

        