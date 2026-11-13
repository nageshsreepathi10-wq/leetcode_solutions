class Solution:
    def arraySign(self, nums: list[int]) -> int:
        n=1
        for i in nums:
            n=n*i
        if n<0:
            return -1
        elif n>0:
            return 1
        else:
            return 0
        
            