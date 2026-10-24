class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        li=[]
        nums.sort()
        for i in  range(len(nums)):
            if nums[i]==target:
                li.append(i)
        return li