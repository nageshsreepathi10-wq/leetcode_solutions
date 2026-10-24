class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        min=nums[0]*nums[1]
        max=nums[-1]*nums[-2]
        product=max-min
        return product