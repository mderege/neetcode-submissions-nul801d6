class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictNums = {}
        for i in range(len(nums)):
            dictNums[nums[i]] = i
        seqStart = []
        for i in nums:
            if i-1 not in dictNums:
                seqStart.append(i)
        seq = False
        count = 0
        seqCount = []
        print(seqStart)
        for i in seqStart:
            seq = True
            count = 1
            curr = i
            while seq:
                if curr+1 in dictNums:
                    count +=1
                    curr +=1
                else:
                    seq = False
            seqCount.append(count)
        print(seqCount)
        highest = 0
        for i in seqCount:
            if i > highest:
                highest = i

        return highest
        
        


        
        
        


        

        # for i in nums:
        #     if i-1 not in dictNums and dictNums[i-1] < dictNums[i]:
        #         seqStart.append(i)
        #     elif i-1 in dictNums and dictNums[i-1] < dictNums[i]:
        # seq = False
        # count = 0
        # seqCount = []
        # print(seqStart)
        # for i in seqStart:
        #     seq = True
        #     count = 1
        #     curr = i
        #     while seq:
        #         if curr+1 in dictNums and dictNums[curr] < dictNums[curr+1]:
        #             count +=1
        #             curr +=1
        #         else:
        #             seq = False
        #     seqCount.append(count)
        # print(seqCount)
        # return 0
        
        


        