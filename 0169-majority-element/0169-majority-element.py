class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        ans=max(dict,key=dict.get)
        return ans

        