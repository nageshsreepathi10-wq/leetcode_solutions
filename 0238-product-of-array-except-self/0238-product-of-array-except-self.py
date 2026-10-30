class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        list=[0]*len(nums)
        list[0]=1
        for i in range(1,len(nums)):
            list[i]=list[i-1]*nums[i-1]
        right=1
        for j in range(len(nums)-1,-1,-1):
            list[j]*=right
            right*=nums[j]
        return list
    


