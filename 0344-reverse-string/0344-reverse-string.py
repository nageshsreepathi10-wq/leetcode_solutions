class Solution:
    def reverseString(self, nums: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(nums)-1
        while l!=len(nums)//2:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
                