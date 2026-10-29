class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefixsum=0
        dict={0:1}
        for i in nums:
            prefixsum+=i
            if prefixsum-k in dict:
                count+=dict[prefixsum-k]
            if prefixsum not in dict:
                dict[prefixsum]=1
            else:
                dict[prefixsum]+=1
        return count 


    

