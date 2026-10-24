class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        b=[]
        i=0
        while i<k:
            a=max(dict,key=dict.get)
            b.append(a)
            del dict[a]
            i+=1
        return b