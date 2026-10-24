class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if (n-1)%2==0:
            n1=n//2
            res=nums1[n1]
        else:
            res=(nums1[n//2]+nums1[(n//2)-1])/2
        return res


