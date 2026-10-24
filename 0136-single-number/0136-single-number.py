class Solution:
    def singleNumber(self, l: List[int]) -> int:
        a=0
        for i in l:
            a=a^i
        return a
        