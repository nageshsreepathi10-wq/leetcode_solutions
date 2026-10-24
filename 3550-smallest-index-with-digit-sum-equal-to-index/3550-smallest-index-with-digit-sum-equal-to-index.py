class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum=0
            while nums[i]>0:
                temp=nums[i]%10
                sum+=temp
                nums[i]=nums[i]//10
            if i==sum:
                return i
        else:
            return -1
        