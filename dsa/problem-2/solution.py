class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        l, h = 0, m
        while l <= h:
            c1 = (l+h)//2
            c2 = (m+n+1)//2 - c1
            l1 = float('-inf') if c1 == 0 else nums1[c1-1]
            r1 = float('inf') if c1 == m else nums1[c1]
            l2 = float('-inf') if c2 == 0 else nums2[c2 - 1]
            r2 = float('inf') if c2 == n else nums2[c2]
            if l1 <= r2 and l2 <= r1:
                if(m+n)%2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l1 > r2:
                h = c1 - 1
            else:
                l = c1 + 1
