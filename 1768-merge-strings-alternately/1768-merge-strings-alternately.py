class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        min_len=min(n,m)
        s=""
        i=0
        while i<min_len:
            s+=word1[i]
            s+=word2[i]
            i+=1
        if n<m:
            s+=word2[min_len:]
        else:
            s+=word1[min_len:]
        return s