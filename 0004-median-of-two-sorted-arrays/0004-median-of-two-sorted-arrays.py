class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n3 = nums1 + nums2
        n3.sort()
        i = len(n3)

        if i%2 == 1:
            return float(n3[i // 2])
        else:
            m1 = n3[i // 2 - 1]
            m2 = n3[i // 2]
            return ((float(m1) + float(m2)) / 2.0)
