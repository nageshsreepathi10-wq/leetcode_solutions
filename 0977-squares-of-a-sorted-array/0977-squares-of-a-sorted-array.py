class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=[]
        for i in nums:
            n1=i*i
            n.append(n1)
        n.sort()
        return n