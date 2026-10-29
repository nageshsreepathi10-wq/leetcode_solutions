class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        word=""
        for i in words:
            if i==i[::-1]:
                word=i
                break
        return word
        