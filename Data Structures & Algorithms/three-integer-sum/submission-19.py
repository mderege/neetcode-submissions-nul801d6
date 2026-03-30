class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       triplets = []
       currTrip = []
       curr = len(nums)-1
       nextVal =  len(nums)-2
       for i in range(len(nums)):
            total = nums[curr] + nums[nextVal]
            while i < curr:
                total = nums[curr] + nums[nextVal]
                while (nums[i]*(-1)) < total and nextVal > i:
                    total -= nums[nextVal]
                    nextVal -=1
                    total += nums[nextVal]
                    print(total)
                    if total == nums[i]*(-1) and (nextVal != curr) and (i != nextVal) and (i != curr):
                        currTrip.append(nums[i])
                        currTrip.append(nums[curr])
                        currTrip.append(nums[nextVal])
                        
                if len(currTrip) == 0:
                    if total == nums[i]*(-1) and (nextVal != curr) and (i != nextVal) and (i != curr):
                        currTrip.append(nums[i])
                        currTrip.append(nums[curr])
                        currTrip.append(nums[nextVal])
                if len(currTrip) != 0:
                    currTrip.sort()
                    if currTrip not in triplets:
                        triplets.append(currTrip)
                curr -= 1
                nextVal = curr - 1
                currTrip = []
            curr = len(nums)-1
            nextVal = len(nums)-2
       return triplets