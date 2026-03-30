class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        def main(index):
            if index >= len(nums):
                result.append(curr.copy()) # this is becuase 
                #you reached the leaf node and want to add full path to result list
                return 
            
            #this includes current index
            curr.append(nums[index])
            main(index+1)

            curr.pop()
            main(index+1)
            
        main(0)
        return result