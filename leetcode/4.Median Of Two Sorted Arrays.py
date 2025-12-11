import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2): 
            A, B = B, A

        l, r = 0, len(A) -1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            ALeft = nums1[i] if i >= 0 else -math.inf
            ARight = nums1[i + 1] if (i + 1) < len(nums1) else math.inf
            BLeft = nums2[j] if j >= 0 else -math.inf
            BRight = nums2[j + 1] if (j + 1) < len(nums1) else math.inf

            if (ALeft <= BRight and ARight >= BLeft):
                if(total % 2):
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                return min(ARight, BRight)
            
            if(ALeft > BRight):
                r = i - 1
            else:
                r = i + 1

