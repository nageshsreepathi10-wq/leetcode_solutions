class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".lower()
        for ch in s:
            if ch.isalnum():
                result += ch.lower()

        if result[::-1]==result:
            return True
        else:
            return False
        