class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            elif i in dict:
                dict[i]+=1
        res=False
        for j in dict:
            if dict[j]>1:
                res=True
                break
        return res
            