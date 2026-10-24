class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s1=" "
        for i in s[::-1]:
            s1+=i+" "
        return s1.strip()
            