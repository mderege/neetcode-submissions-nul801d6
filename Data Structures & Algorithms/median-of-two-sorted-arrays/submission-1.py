class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1)+len(nums2))//2
        A = []
        B = []
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1 
        l = 0
        r = len(A)-1
        while True:
            mid = ((r-l)//2)+l
            Aleft = A[mid] if mid >= 0 else -math.inf
            Aright = A[mid+1] if mid+1 <(len(A)) else math.inf
            Bleft = B[half-mid-2] if half-mid-2 >= 0 else -math.inf
            Bright = B[half-mid-1] if half-mid-1 < len(B) else math.inf
            
            if  Bleft <= Aright and Aleft <= Bright:
                if (len(A)+len(B))%2 == 0:
                    return (max(Aleft, Bleft)+min(Aright, Bright))/2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = mid-1
            elif Bleft > Aright:
                l = mid+1
        