class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        n1=[]
        l=0
        r=n//2
        while l<n//2:
            n1.append(nums[l])
            n1.append(nums[r])
            l+=1
            r+=1
        return n1